"""Film o szefie (26.11.2026): sceny z jego avatarem - FLUX Kontext (HF, darmowo) z referencja szef.png."""
import sys, shutil, pathlib, time, subprocess
sys.path.insert(0, r"C:\Hexa\generatory")
from gradio_client import handle_file
from hexa_gen import client
OUT = pathlib.Path(r"C:\Hexa\lab\film_szef")
REF = r"C:\Hexa\generatory\szef.png"
BASE = ("Keep exactly the same man and his face identity: short dark hair styled up with shaved sides, thin dark goatee, dark sunglasses, strong jaw. "
        "Re-render the whole image as a high-end stylized 3D animated feature film still, modern cyberpunk world, neon cyan and warm gold lights, "
        "cinematic lighting, depth of field, rich detail, no text, no letters, no words, no logos, screens show only abstract lines and candles. He is always dressed elegantly and with class. Scene: ")
S = {
 "s1": "dawn in a rainy neon cyberpunk street, he waits at a tram stop in an elegant dark wool overcoat over a tailored suit, tired but composed, wet reflections, glowing holographic clock in the air",
 "s2": "inside a huge industrial warehouse with conveyor belts and orange safety lights, he wears a crisp shirt and a dark waistcoat, looking up at a big wall clock, grey monotony around him",
 "s3": "late night in a small apartment, he sits at a desk with three glowing monitors showing gold price candlestick charts, rain on the window, neon city outside, white shirt with rolled sleeves and waistcoat",
 "s4": "close shot at night, he writes in a leather notebook full of handwritten notes and small charts under a warm desk lamp, a cup of coffee, monitors glowing cyan behind",
 "s5": "he stands in an elegant suit in front of a wall of floating holographic trading charts with a large glowing golden zen circle in the middle, thinking, calm and focused",
 "s6": "a futuristic glowing cyan server room, streams of holographic data and small friendly robot icons trading, he observes calmly in a tailored three-piece suit",
 "s7": "sunrise, he walks confidently out through an open industrial factory gate in a tailored navy suit, the gate and the grey factory behind him, golden light ahead",
 "s8": "golden sunrise on a rooftop terrace above a gleaming cyberpunk skyline, he stands in an elegant suit holding a coffee, relaxed slight smile, free",
}
c = client("black-forest-labs/FLUX.1-Kontext-Dev")
wybrane = sys.argv[1:] or list(S)
for k in wybrane:
    dst = OUT / f"{k}.jpg"
    if dst.exists(): print(k, "jest"); continue
    for proba in range(2):
        try:
            t0 = time.time()
            r = c.predict(input_image=handle_file(REF), prompt=BASE + S[k], randomize_seed=True, guidance_scale=2.5, steps=28, api_name="/infer")
            p = r[0]["path"] if isinstance(r[0], dict) else r[0]
            from PIL import Image
            Image.open(p).convert("RGB").save(dst, quality=93)
            print(k, "OK", int(time.time() - t0), "s", flush=True); break
        except Exception as e:
            print(k, "blad", str(e)[:200], flush=True); time.sleep(20)
print("KONIEC", flush=True)
