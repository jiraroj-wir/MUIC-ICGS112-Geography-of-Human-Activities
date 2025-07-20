import os
import markdown
from weasyprint import HTML, CSS

# Paths
DOCS_DIR = "docs"
OUTPUT_DIR = "pdf"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Dark theme CSS
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

# Process all Markdown files in docs/
for filename in os.listdir(DOCS_DIR):
    if filename.endswith(".md"):
        src_path = os.path.join(DOCS_DIR, filename)
        base = os.path.splitext(filename)[0]

        with open(src_path, encoding="utf-8") as f:
            md = f.read()

        # Convert Markdown to HTML
        html = markdown.markdown(
            md, extensions=["extra", "codehilite", "tables", "toc"]
        )

        # Light theme PDF
        light_pdf_path = os.path.join(OUTPUT_DIR, f"{base}.pdf")
        HTML(string=html).write_pdf(light_pdf_path)
        print(f"Generated {light_pdf_path}")

        # Dark theme PDF
        dark_pdf_path = os.path.join(OUTPUT_DIR, f"{base}-dark.pdf")
        HTML(string=html).write_pdf(dark_pdf_path, stylesheets=[CSS(string=DARK_CSS)])
        print(f"Generated {dark_pdf_path}")
