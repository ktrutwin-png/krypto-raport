"""FLUX.2 [dev] na Cloudflare Workers AI (darmowa dzienna pula) z obrazem referencyjnym – postac szefa w nowych scenach. 26.11.2026.
Uzycie: python flux2_ref.py "prompt EN" wynik.jpg [ref.jpg] [szer] [wys]"""
import sys, json, base64, requests
k = open(r"C:\Hexa\sejf\cloudflare.txt", encoding="utf-8").read().strip()
acc = open(r"C:\Hexa\sejf\cloudflare_konto.txt", encoding="utf-8").read().strip()
prompt, out = sys.argv[1], sys.argv[2]
ref = sys.argv[3] if len(sys.argv) > 3 else r"C:\Hexa\generatory\szef_avatar.jpg"
w = sys.argv[4] if len(sys.argv) > 4 else "768"; h = sys.argv[5] if len(sys.argv) > 5 else "1344"
files = {"prompt": (None, prompt), "width": (None, w), "height": (None, h), "steps": (None, "25"),
         "input_image_0": ("ref.jpg", open(ref, "rb"), "image/jpeg")}
r = requests.post(f"https://api.cloudflare.com/client/v4/accounts/{acc}/ai/run/@cf/black-forest-labs/flux-2-dev",
                  headers={"Authorization": f"Bearer {k}"}, files=files, timeout=180)
j = r.json()
if not j.get("success"): sys.exit("BLAD " + json.dumps(j.get("errors"))[:400])
open(out, "wb").write(base64.b64decode(j["result"]["image"])); print(out)
