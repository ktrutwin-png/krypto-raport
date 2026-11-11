// node shot.js <mode:still|video> [w] [h] [frames]
const { chromium } = require('playwright');
const http = require('http'); const fs = require('fs'); const path = require('path');
const root = __dirname;
const mime = { '.html': 'text/html', '.js': 'text/javascript' };
const srv = http.createServer((q, r) => {
  const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream' }); r.end(d); });
}).listen(8731);
(async () => {
  const [mode = 'still', w = 1080, h = 1350, frames = 150] = process.argv.slice(2);
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: +w, height: +h } });
  p.on('console', m => { if (m.type() === 'error') console.log('ERR', m.text()); });
  p.on('pageerror', e => console.log('PAGEERR', e.message));
  await p.goto(`http://localhost:8731/scena_zloto.html?w=${w}&h=${h}`);
  await p.waitForFunction('window.ready === true', null, { timeout: 60000 });
  if (mode === 'still') {
    await p.evaluate(() => window.renderAt(1.05));
    await p.screenshot({ path: path.join(root, 'still.png') });
  } else {
    fs.mkdirSync(path.join(root, 'frames'), { recursive: true });
    for (let i = 0; i < +frames; i++) {
      await p.evaluate(t => window.renderAt(t), i / 30);
      await p.screenshot({ path: path.join(root, 'frames', `f${String(i).padStart(4, '0')}.png`) });
      if (i % 30 === 0) console.log('frame', i);
    }
  }
  await b.close(); srv.close();
})();
