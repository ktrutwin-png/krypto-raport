# Daily Reel pipeline (erl.grey83)

Template for the 15:00 (Europe/Amsterdam) daily Reel and the Sunday 22:00 weekly summary Reel.
Copy this folder to a scratchpad, then:

1. Edit `reel.html`: scenes sc1..sc6 (hook with big number + 7-day BTC chart from `prices.js`, why/cause scene, drivers, funds, levels + key dates, CTA question). Keep all on-screen text in English, nick @erl.grey83, footer "For information only, not investment advice."
   Replace `PX` in `prices.js` with fresh 7-day BTC prices (CoinGecko get-coin-market-chart, id=bitcoin, days=7).
2. Edit `segs` in `vo.py` - narration explains WHY it happened (do not read the slide text), only facts from >=2 sources, hedge causes ("analysts point to"). Voice: piper en_US-joe-medium (deep male, ~95 Hz). Download once:
   `curl -L -o voice/en_US-joe-medium.onnx https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` (+ `.onnx.json`). Needs `pip install --break-system-packages piper-tts` and `export no_proxy= NO_PROXY=` for pip/curl.
3. `python3 vo.py` -> timing.json + voice.m4a. `python3 music.py <T>` -> melody.wav (original calm melody), then `ffmpeg -i melody.wav -af "lowpass=f=3500,aecho=0.8:0.55:380|760:0.3|0.2" melody_fx.wav`.
4. Frames: run 4 in parallel `python3 frames.py <i> 4` (i=0..3) -> f/%05d.jpg (30 fps, 1080x1920).
5. Mix (music ducked under voice, loudnorm) and mux:
   `ffmpeg -i melody_fx.wav -i voice.m4a -filter_complex "[0]aresample=44100,aformat=channel_layouts=stereo,volume=0.55[m];[1]aresample=44100,aformat=channel_layouts=stereo,equalizer=f=140:t=q:w=1:g=3,asplit[v1][v2];[m][v1]sidechaincompress=threshold=0.015:ratio=5:attack=30:release=600:makeup=1[duck];[duck][v2]amix=inputs=2:normalize=0:weights=1 1.2,loudnorm=I=-15:TP=-1.5:LRA=7[out]" -map "[out]" -ar 44100 -c:a aac -b:a 160k mix.m4a`
   `ffmpeg -framerate 30 -i f/%05d.jpg -i mix.m4a -shortest -c:v libx264 -pix_fmt yuv420p -crf 21 -movflags +faststart reel.mp4`
6. Cover = a frame around 5-6 s (jpg). Push mp4 + cover + caption.txt to `reports/YYYY-MM-DD-reel/`, publish with Windsor `create_video_post` (raw GitHub URLs, share_to_feed true).
Caption: hook first line, 3 facts, a question for comments, "Follow @erl.grey83", disclaimer, 5-8 hashtags.
