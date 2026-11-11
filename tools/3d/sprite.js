// node sprite.js  -> sprite_<coin>.png (8x6 klatek po 256px, przezroczyste tło)
const { chromium } = require('playwright'); const http = require('http'); const fs = require('fs'); const path = require('path');
const root = __dirname; const mime = { '.html': 'text/html', '.js': 'text/javascript' };
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); return r.end(); } r.writeHead(200, { 'Content-Type': mime[path.extname(f)] || 'application/octet-stream' }); r.end(d); }); }).listen(8732);
(async () => {
  const S = 256, N = 48;
  const b = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const p = await b.newPage({ viewport: { width: S, height: S } });
  p.on('pageerror', e => console.log('PAGEERR', e.message));
  await p.goto(`http://localhost:8732/monety_sprite.html?w=${S}&h=${S}`);
  await p.waitForFunction('window.ready === true', null, { timeout: 60000 });
  fs.mkdirSync(path.join(root, 'sprite_frames'), { recursive: true });
  for (const k of ['btc', 'eth', 'au']) {
    await p.evaluate(k => window.setCoin(k), k);
    for (let i = 0; i < N; i++) {
      await p.evaluate(t => window.renderAt(t), i / N);
      await p.screenshot({ path: path.join(root, 'sprite_frames', `${k}_${String(i).padStart(2, '0')}.png`), omitBackground: true });
    }
    console.log('done', k);
  }
  await b.close(); srv.close();
})();
