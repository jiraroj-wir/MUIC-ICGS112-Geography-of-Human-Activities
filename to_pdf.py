import os
import markdown
from weasyprint import HTML, CSS

# paths
docs = "docs"
files = ["lecture.md", "questions.md"]

# dark theme CSS
DARK_CSS = """
@page { size: A4; margin: 0; background: #111; }
body {
    background: #111 !important;
    color: #eee !important;
    margin: 0;
    font-family: 'DejaVu Sans', Arial, sans-serif;
}
h1, h2, h3, h4, h5, h6 { color: #fff !important; }
a { color: #80b3ff !important; }
pre, code {
    background: #222 !important;
    color: #cfc !important;
    border-radius: 4px;
    padding: 2px 4px;
}
"""

for filename in files:
    src_path = os.path.join(docs, filename)
    base = os.path.splitext(filename)[0]
    with open(src_path, encoding="utf-8") as f:
        md = f.read()
    html = markdown.markdown(md, extensions=["extra", "codehilite", "tables", "toc"])

    # light theme PDF
    HTML(string=html).write_pdf(os.path.join(docs, f"{base}.pdf"))
    print(f"Generated {base}.pdf")

    # dark theme PDF
    HTML(string=html).write_pdf(
        os.path.join(docs, f"{base}-dark.pdf"), stylesheets=[CSS(string=DARK_CSS)]
    )
    print(f"Generated {base}-dark.pdf")
