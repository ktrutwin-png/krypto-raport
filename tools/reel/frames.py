import json,os,sys
from playwright.sync_api import sync_playwright
tm=json.load(open('timing.json'));FPS=30;T=tm['T']
os.makedirs('f',exist_ok=True)
part,parts=int(sys.argv[1]),int(sys.argv[2])
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.on('pageerror',lambda e:print('ERR',e))
    pg.goto('file://'+os.path.abspath('reel.html'));pg.wait_for_timeout(500)
    pg.evaluate('S='+json.dumps(tm['S'])+';T='+str(T))
    n=int(T*FPS)
    if part<0:
        for t in sys.argv[3:]:
            pg.evaluate(f'render({t})');pg.locator('canvas').screenshot(path=f'p_{t}.png')
    else:
        for i in range(part,n,parts):
            pg.evaluate(f'render({i/FPS})');pg.locator('canvas').screenshot(path=f'f/{i:05d}.jpg',type='jpeg',quality=90)
    b.close()
