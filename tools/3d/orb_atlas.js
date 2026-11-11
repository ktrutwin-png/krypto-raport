// Atlas klatek bryły 3D roju Hexa dla aplikacji ORB.
//   node orb_atlas.js <hexa|dron> <out_dir> <rozmiar_px> <krok_pitch> <max_pitch> <krok_yaw>
//   podgląd jednej klatki: node orb_atlas.js <model> <out.png> <px> --one <pitch> <yaw>
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const root = __dirname;
const [m = 'hexa', out = 'atlas', S = '400', a4 = '15', a5 = '60', a6 = '10', a7, a8] = process.argv.slice(2);
const mime = { '.html': 'text/html', '.js': 'text/javascript' };
const srv = http.createServer((q, r) => {
  const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  if (!f.startsWith(root)) { r.writeHead(403); return r.end(); }
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
});
srv.listen(0, async () => {
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: +S, height: +S } });
  p.on('pageerror', e => console.error('ERR', e.message));
  await p.goto(`http://localhost:${srv.address().port}/orb_modele.html?m=${m}&s=${S}`);
  await p.waitForFunction('window.ready === true', null, { timeout: 60000 });
  const save = (file, url) => fs.writeFileSync(file, Buffer.from(url.split(',')[1], 'base64'));
  if (a4 === '--one') { save(out, await p.evaluate(([x, y]) => window.frame(x, y), [+a5, +a6])); }
  else {
    fs.mkdirSync(out, { recursive: true }); let n = 0;
    for (let pt = -(+a5); pt <= +a5; pt += +a4) for (let yw = 0; yw < 360; yw += +a6) {
      save(path.join(out, `${m[0]}_${pt + 90}_${yw}.png`), await p.evaluate(([x, y]) => window.frame(x, y), [pt, yw])); n++; }
    console.log('klatek', n);
  }
  await b.close(); srv.close();
});
