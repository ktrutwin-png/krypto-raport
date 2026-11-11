// Render sceny 3D do filmu (tlo sceny w kino.py) albo do jednej klatki.
//   node scena.js <typ> '<json parametrow>' <out.mp4|out.jpg> [sekundy=4] [w=1080] [h=1920] [fps=30]
//   typy: liczba | waga | swiece | pokretlo | skarbiec | globus   (parametry: README.md)
// out.jpg/png = jedna klatka (z konca ruchu); out.mp4 = film. Wymaga: npm i (three) w tym folderze + ffmpeg.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const root = __dirname;
const [typ = 'liczba', pj = '{}', out = 'scena.mp4', sek = 4, w = 1080, h = 1920, fps = 30] = process.argv.slice(2);
JSON.parse(pj);                                               // zly JSON = blad od razu, nie po renderze
const mime = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json' };
const srv = http.createServer((q, r) => {
  const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  if (!f.startsWith(root)) { r.writeHead(403); return r.end(); }
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
srv.listen(0, async () => {
  const port = srv.address().port, still = /\.(jpe?g|png)$/i.test(out);
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  let bad = '';
  p.on('console', m => { if (m.type() === 'error') bad += m.text() + '\n'; });
  p.on('pageerror', e => { bad += e.message + '\n'; });
  try {
    await p.goto(`http://localhost:${port}/sceny3d.html?typ=${typ}&w=${w}&h=${h}&d=${sek}&p=${encodeURIComponent(pj)}`);
    await p.waitForFunction('window.ready === true', null, { timeout: 120000 });
    if (still) {
      await p.evaluate(t => window.renderAt(t), +sek * 0.8);
      await p.screenshot({ path: out, type: /png$/i.test(out) ? 'png' : 'jpeg', ...(/png$/i.test(out) ? {} : { quality: 94 }) });
    } else {
      const dir = fs.mkdtempSync(path.join(require('os').tmpdir(), 'scena3d-')), n = Math.round(+sek * +fps);
      for (let i = 0; i < n; i++) {
        await p.evaluate(t => window.renderAt(t), i / +fps);
        await p.screenshot({ path: path.join(dir, `f${String(i).padStart(4, '0')}.jpg`), type: 'jpeg', quality: 95 });
      }
      execFileSync('ffmpeg', ['-y', '-v', 'error', '-framerate', String(fps), '-i', path.join(dir, 'f%04d.jpg'), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p', out]);
      fs.rmSync(dir, { recursive: true, force: true });
    }
    console.log(out, typ, still ? 'klatka' : `${sek}s`);
  } catch (e) { console.error('BLAD:', e.message, bad); process.exitCode = 1; }
  await b.close(); srv.close();
});
