const {chromium}=require('playwright');const fs=require('fs'),{execFileSync}=require('child_process');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/neon_r.html');await p.waitForFunction('window.ready===true');
const still=process.argv[2]==='still';
if(still){for(const t of [1.2,4,7.5]){await p.evaluate(t=>window.renderAt(t),t);await p.screenshot({path:`k_${t}.jpg`,type:'jpeg',quality:90})}}
else{fs.mkdirSync('fr',{recursive:true});const N=9*30;for(let i=0;i<N;i++){await p.evaluate(t=>window.renderAt(t),i/30);await p.screenshot({path:`fr/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:92})}
execFileSync('ffmpeg',['-y','-v','error','-framerate','30','-i','fr/f%04d.jpg','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-shortest','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-c:a','aac','neon_brief.mp4'])}
await b.close()})();
