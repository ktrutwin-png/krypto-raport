from playwright.sync_api import sync_playwright
import pathlib
p=pathlib.Path(__file__).parent.resolve()
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for s in range(0,7):
        pg.goto(f"file://{p}/karta_en.html?step={s}"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(p/f"klatka_{s}.png"))
    b.close()
