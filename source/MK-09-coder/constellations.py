#!/usr/bin/env python3
from __future__ import annotations
import argparse, random, sys, os, unicodedata
from typing import Dict, List, Tuple

Cell = str
Point = Tuple[int, int]
Catalog = Dict[str, List[Tuple[Tuple[float,float], Tuple[float,float]]]]

# 88 IAU constellations (menu order)
CONSTELLATIONS = [
    "Andromeda","Antlia","Apus","Aquarius","Aquila","Ara","Aries","Auriga","Boötes","Caelum",
    "Camelopardalis","Cancer","Canes Venatici","Canis Major","Canis Minor","Capricornus","Carina",
    "Cassiopeia","Centaurus","Cepheus","Cetus","Chamaeleon","Circinus","Columba","Coma Berenices",
    "Corona Australis","Corona Borealis","Corvus","Crater","Crux","Cygnus","Delphinus","Dorado","Draco",
    "Equuleus","Eridanus","Fornax","Gemini","Grus","Hercules","Horologium","Hydra","Hydrus","Indus",
    "Lacerta","Leo","Leo Minor","Lepus","Libra","Lupus","Lynx","Lyra","Mensa","Microscopium","Monoceros",
    "Musca","Norma","Octans","Ophiuchus","Orion","Pavo","Pegasus","Perseus","Phoenix","Pictor","Pisces",
    "Piscis Austrinus","Puppis","Pyxis","Reticulum","Sagitta","Sagittarius","Scorpius","Sculptor","Scutum",
    "Serpens","Sextans","Taurus","Telescopium","Triangulum","Triangulum Australe","Tucana","Ursa Major",
    "Ursa Minor","Vela","Virgo","Volans","Vulpecula"
]

# --- utils / name normalization ---
def _strip_accents_lower(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return " ".join(s.lower().split())

ALIASES = {
    "corona austrina": "corona australis",   # common alt spelling
    "serpens caput": "serpens",
    "serpens cauda": "serpens",
    "bootes": "boötes",                       # menu has the umlaut
}

# --- drawing primitives ---
def bresenham(x0: int, y0: int, x1: int, y1: int) -> List[Point]:
    pts: List[Point] = []
    dx = abs(x1 - x0); sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0); sy = 1 if y0 < y1 else -1
    err = dx + dy
    x, y = x0, y0
    while True:
        pts.append((x, y))
        if x == x1 and y == y1: break
        e2 = 2 * err
        if e2 >= dy:
            err += dy; x += sx
        if e2 <= dx:
            err += dx; y += sy
    return pts

def make_canvas(w: int, h: int, char: Cell = " ") -> List[List[Cell]]:
    return [[char for _ in range(w)] for _ in range(h)]

def put_star(canvas: List[List[Cell]], x: int, y: int, bright: bool = False) -> None:
    if 0 <= y < len(canvas) and 0 <= x % len(canvas[0]) < len(canvas[0]):
        canvas[y][x % len(canvas[0])] = "✶" if bright else "*"

def draw_line_wrap(canvas: List[List[Cell]], a: Point, b: Point) -> None:
    """
    Draw a solid line handling X wrap (0..w-1). If |x2-x1| > w/2, we draw across the edge.
    """
    w, h = len(canvas[0]), len(canvas)
    (x1, y1), (x2, y2) = a, b

    # choose the shorter direction in x by allowing a virtual wrap
    if abs(x2 - x1) <= w // 2:
        xA, yA, xB, yB = x1, y1, x2, y2
    else:
        # wrap one endpoint horizontally
        if x1 < x2:
            xA, yA, xB, yB = x1 + w, y1, x2, y2
        else:
            xA, yA, xB, yB = x1, y1, x2 + w, y2

    for (x, y) in bresenham(xA, yA, xB, yB):
        if 0 <= y < h:
            xm = x % w
            if canvas[y][xm] not in ("*", "✶", "●", "o"):
                canvas[y][xm] = "-"

# --- projection ---
def project_radec_to_xy(ra_deg: float, dec_deg: float, w: int, h: int, mirror: bool) -> Point:
    """
    Equirectangular projection to screen. RA in 0..360.
    mirror=True flips RA left↔right (classic sky charts).
    """
    ra = ra_deg % 360.0
    x = int((ra / 360.0) * (w - 1))
    if mirror:  # flip horizontally
        x = (w - 1) - x
    y = int(((90.0 - dec_deg) / 180.0) * (h - 1))
    return (max(0, min(w - 1, x)), max(0, min(h - 1, y)))

def lon_to_ra(lon_deg: float, source: str) -> float:
    """
    Map dataset longitude to RA degrees.
    - source='d3' : RA = (-lon) % 360  (d3-celestial / Stellarium exports)
    - source='ra' : RA = lon % 360     (file already stores RA in degrees)
    """
    if source == "d3":
        return (-lon_deg) % 360.0
    return lon_deg % 360.0

# --- catalog loader ---
def load_catalog_tsv(path: str) -> Catalog:
    """
    Accepts TSV with either:
      name  ra1  dec1  ra2  dec2
    or:
      name  seg_i  ra1  dec1  ra2  dec2
    Skips header; tolerant to mixed whitespace.
    """
    segs: Catalog = {}
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) not in (5, 6):
                parts = line.split()
                if len(parts) not in (5, 6):
                    continue
            # header?
            if _strip_accents_lower(parts[0]) == "name":
                continue
            try:
                if len(parts) == 5:
                    name, a1, d1, a2, d2 = parts[0], float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])
                else:
                    name, _seg, a1, d1, a2, d2 = parts[0], parts[1], float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])
            except ValueError:
                continue
            key = ALIASES.get(_strip_accents_lower(name), _strip_accents_lower(name))
            segs.setdefault(key, []).append(((a1, d1), (a2, d2)))
    return segs

# --- rendering a single constellation ---
def draw_constellation(canvas: List[List[Cell]], menu_name: str,
                       segments: List[Tuple[Tuple[float,float], Tuple[float,float]]],
                       source: str, mirror: bool) -> None:
    """
    segments coordinates are in the TSV as lon/lat (if source='d3') or RA/Dec (if source='ra').
    """
    w, h = len(canvas[0]), len(canvas)
    node_pts: set[Point] = set()

    # Project every segment to screen (wrap-aware lines)
    for ((A1, D1), (A2, D2)) in segments:
        # Map to RA if needed
        ra1 = lon_to_ra(A1, source)
        ra2 = lon_to_ra(A2, source)
        x1, y1 = project_radec_to_xy(ra1, D1, w, h, mirror)
        x2, y2 = project_radec_to_xy(ra2, D2, w, h, mirror)
        draw_line_wrap(canvas, (x1, y1), (x2, y2))
        node_pts.add((x1, y1)); node_pts.add((x2, y2))

    # brighten nodes last
    for (x, y) in node_pts:
        put_star(canvas, x, y, bright=True)

# --- UI helpers ---
def show_menu() -> int:
    print("\nChoose a constellation by number (0 to quit):\n")
    for i, name in enumerate(CONSTELLATIONS, 1):
        print(f"{i:2d}. {name}")
    print()
    try:
        return int(input("Your choice: ").strip())
    except Exception:
        return -1

def render_selection(name: str, catalog: Catalog, w: int, h: int, labels: bool, source: str, mirror: bool) -> str:
    canvas = make_canvas(w, h, " ")
    key = ALIASES.get(_strip_accents_lower(name), _strip_accents_lower(name))

    if key not in catalog or not catalog[key]:
        msg = f"[!] No segments for '{name}' found in catalog. Please add its lines to the TSV."
        row = h // 2; col = max(0, (w - len(msg)) // 2)
        for i, ch in enumerate(msg):
            if 0 <= col + i < w:
                canvas[row][col + i] = ch
        return "\n".join("".join(r) for r in canvas)

    # starry background (ambience)
    rng = random.Random(hash(key) & 0xFFFFFFFF)
    for _ in range((w * h) // 60):
        x, y = rng.randrange(0, w), rng.randrange(0, h)
        if canvas[y][x] == " ":
            canvas[y][x] = "." if rng.random() < 0.7 else "·"

    draw_constellation(canvas, name, catalog[key], source, mirror)

    if labels:
        title = f"*** {name} ***"
        row = 1; col = max(0, (w - len(title)) // 2)
        if row < h:
            for i, ch in enumerate(title):
                if 0 <= col + i < w:
                    canvas[row][col + i] = ch

    return "\n".join("".join(r) for r in canvas)

def main():
    ap = argparse.ArgumentParser(description="Render accurate constellation stick-figures from a TSV catalog.")
    ap.add_argument("--catalog", required=True, help="Path to TSV: name  ra1/ln1  dec1  ra2/ln2  dec2  (or with seg_i).")
    ap.add_argument("--source", choices=["d3","ra"], default="d3",
                    help="How to interpret the 1st/3rd columns (lon vs RA). d3: RA=(-lon)%%360 (default). ra: RA=lon%%360.")
    ap.add_argument("--width", type=int, default=100, help="Canvas width (cols)")
    ap.add_argument("--height", type=int, default=30, help="Canvas height (rows)")
    ap.add_argument("--mirror", action="store_true", help="Flip RA left↔right like classic sky charts")
    ap.add_argument("--labels", action="store_true", help="Show title label")
    ap.add_argument("--loop", action="store_true", help="Keep choosing constellations until 0")
    args = ap.parse_args()

    if not os.path.exists(args.catalog):
        print(f"Catalog not found: {args.catalog}", file=sys.stderr)
        sys.exit(1)

    catalog = load_catalog_tsv(args.catalog)
    if not catalog:
        print("Catalog loaded but empty / unparsable.", file=sys.stderr)

    w = max(40, args.width)
    h = max(15, args.height)

    def cycle() -> bool:
        sel = show_menu()
        if sel == 0:
            return False
        if 1 <= sel <= len(CONSTELLATIONS):
            name = CONSTELLATIONS[sel - 1]
            art = render_selection(name, catalog, w, h, args.labels, args.source, args.mirror)
            print("\n" + art + "\n")
        else:
            print("Invalid choice. Try again.")
        return True

    if args.loop:
        while cycle():
            pass
    else:
        cycle()

if __name__ == "__main__":
    main()