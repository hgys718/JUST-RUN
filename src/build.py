"""Rebuild just-ran-poster-builder.html from src/template.html and src/assets/.

    python3 src/build.py
"""
import base64, pathlib
here = pathlib.Path(__file__).parent
a = here / "assets"
b64 = lambda p: base64.b64encode((a / p).read_bytes()).decode()
out = (here / "template.html").read_text()
for key, val in {
    "%%MUXER%%": (a / "muxer.min.js").read_text(),
    "%%SH%%": b64("sample-coffee.jpg"),
    "%%SV%%": b64("sample-waiting.jpg"),
    "%%FONT%%": b64("futura.otf"),
    "%%LOGO%%": b64("logo.mp4"),
    "%%VLINE%%": b64("vline.mp4"),
    "%%HLINE%%": b64("hline.mp4"),
}.items():
    out = out.replace(key, val)
target = here.parent / "just-ran-poster-builder.html"
target.write_text(out)
print(f"wrote {target} ({len(out)/1e6:.1f} MB)")
