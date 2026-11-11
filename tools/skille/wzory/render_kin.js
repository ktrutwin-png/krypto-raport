const { chromium } = require('playwright'); const { execFileSync } = require('child_process'); const fs = require('fs');
(async () => { const S = process.argv[2], N = 150;
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + S + '/kinetyka.html'); await p.evaluate(async () => { await document.fonts.ready; return 1; }); await p.waitForTimeout(800);
  fs.mkdirSync(S + '/kf', { recursive: true });
  for (let i = 0; i < N; i++) { await p.evaluate(t => { window.seek(t); return 1; }, i / 30); await p.screenshot({ path: `${S}/kf/f${String(i).padStart(4,'0')}.jpg`, type: 'jpeg', quality: 92 }); }
  await b.close();
  execFileSync('ffmpeg', ['-y','-v','error','-framerate','30','-i',`${S}/kf/f%04d.jpg`,'-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',`${S}/kinetyka_demo.mp4`]);
  console.log('ok'); })();
