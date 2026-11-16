# Wstawia do ORB Brain.java ścieżkę przez HEXA RDZEŃ (serwer), z powrotem do starego trybu, gdy serwer nie odpowiada.
import sys, io
p = sys.argv[1]
s = io.open(p, encoding="utf-8").read()
if "askRdzen" in s:
    print("juz jest"); sys.exit(0)
a = "                for (String model : MODELS) {"
b = ("                String viaCore = askRdzen(c, text);\n"
     "                if (viaCore != null) { ans = viaCore; }\n"
     "                else for (String model : MODELS) {")
assert a in s; s = s.replace(a, b, 1)
helper = r'''
    /** HEXA RDZEŃ (16.11.2026): pełny mózg na serwerze – stan agentów, pamięć, zadania dla zespołu. */
    static JSONObject core = null;
    static JSONObject core(Context c) {
        if (core != null) return core;
        try (InputStream in = c.getAssets().open("rdzen.json")) {
            BufferedReader r = new BufferedReader(new InputStreamReader(in, "UTF-8"));
            StringBuilder sb = new StringBuilder(); String ln;
            while ((ln = r.readLine()) != null) sb.append(ln);
            core = new JSONObject(sb.toString());
        } catch (Exception e) { core = new JSONObject(); }
        return core;
    }
    static String askRdzen(Context c, String text) {
        try {
            JSONObject cfg = core(c);
            String url = cfg.optString("url", ""), tok = cfg.optString("token", "");
            if (url.isEmpty() || tok.isEmpty()) return null;
            JSONObject body = new JSONObject().put("text", text)
                    .put("lang", c.getSharedPreferences("hexa", 0).getString("lang", "pl"))
                    .put("teraz", now(c));
            HttpURLConnection h = (HttpURLConnection) new URL(url).openConnection();
            h.setConnectTimeout(4000); h.setReadTimeout(60000);
            h.setRequestMethod("POST"); h.setDoOutput(true);
            h.setRequestProperty("Content-Type", "application/json; charset=utf-8");
            h.setRequestProperty("X-Hexa-Token", tok);
            h.setRequestProperty("X-Claude-Key", key(c));
            try (OutputStream o = h.getOutputStream()) { o.write(body.toString().getBytes("UTF-8")); }
            if (h.getResponseCode() != 200) { Log.w("ORB", "rdzen http " + h.getResponseCode()); return null; }
            StringBuilder sb = new StringBuilder();
            try (BufferedReader r = new BufferedReader(new InputStreamReader(h.getInputStream(), "UTF-8"))) { String ln; while ((ln = r.readLine()) != null) sb.append(ln); }
            String t = new JSONObject(sb.toString()).optString("text", "").trim();
            Log.i("ORB", "rdzen: " + t);
            return t.isEmpty() ? null : t;
        } catch (Exception e) { Log.w("ORB", "rdzen " + e); return null; }
    }
'''
a = "    static String call(String key, JSONObject body) throws Exception {"
assert a in s; s = s.replace(a, helper + "\n" + a, 1)
io.open(p, "w", encoding="utf-8").write(s)
print("ok")
