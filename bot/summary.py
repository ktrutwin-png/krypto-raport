import sqlite3, glob, os
for db in sorted(glob.glob(os.path.expanduser('~/freqtrade/*.sqlite'))):
    try:
        c = sqlite3.connect(db)
        cols = [r[1] for r in c.execute("pragma table_info(trades)")]
        if not cols:
            continue
        closed = c.execute("select count(*), coalesce(sum(close_profit_abs),0), coalesce(sum(case when close_profit_abs>0 then 1 else 0 end),0) from trades where is_open=0").fetchone()
        opn = c.execute("select count(*) from trades where is_open=1").fetchone()[0]
        n, pnl, wins = closed
        wr = (100 * wins / n) if n else 0
        print(f"{os.path.basename(db):28s} zamkniete: {n:4d}  wygrane: {wr:5.1f}%  wynik: {pnl:8.2f} EUR  otwarte: {opn}")
    except Exception as e:
        print(os.path.basename(db), 'blad:', e)
