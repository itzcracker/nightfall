import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
G, C = os.path.join(ROOT, "games"), os.path.join(ROOT, "covers")
OUT = os.path.join(ROOT, "games.json")
EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif")

old = {}
if os.path.exists(OUT):
    try:
        old = {g["slug"]: g for g in json.load(open(OUT, encoding="utf-8"))}
    except Exception:
        pass

covers = {}
if os.path.isdir(C):
    for f in os.listdir(C):
        s, e = os.path.splitext(f)
        if e.lower() in EXT:
            covers[s.lower()] = f

found = {}
if os.path.isdir(G):
    for n in sorted(os.listdir(G)):
        p = os.path.join(G, n)
        if os.path.isdir(p) and os.path.exists(os.path.join(p, "index.html")):
            found[n] = f"games/{n}/index.html"
        elif n.lower().endswith(".html"):
            found[n[:-5]] = f"games/{n}"

out = []
for slug, file in found.items():
    name = old.get(slug, {}).get("name") or re.sub(r"[-_]+", " ", slug).strip().title()
    c = covers.get(slug.lower())
    out.append({"name": name, "slug": slug, "file": file, "cover": f"covers/{c}" if c else None})
out.sort(key=lambda g: g["name"].lower())

json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(out), "games")
