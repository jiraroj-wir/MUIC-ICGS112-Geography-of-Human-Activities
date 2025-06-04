#!/bin/bash
set -e

# install dependencies
pip3 install --quiet markdown weasyprint

# dark theme CSS
cat <<EOF > docs/dark.css
body {
  background: #111 !important;
  color: #eee !important;
}
a { color: #9cf !important; }
pre, code { background: #222 !important; color: #cfc !important; }
h1, h2, h3, h4, h5, h6 { color: #fff !important; }
EOF

for FILE in lecture.md questions.md; do
  SRC="docs/$FILE"
  BASENAME=$(basename "$FILE" .md)
  HTML="docs/${BASENAME}.html"
  PDF="docs/${BASENAME}.pdf"
  PDF_DARK="docs/${BASENAME}-dark.pdf"

  python3 -m markdown "$SRC" > "$HTML"

  # normal PDF
  weasyprint "$HTML" "$PDF"

  # dark PDF
  weasyprint "$HTML" "$PDF_DARK" --stylesheet docs/dark.css

  echo "Converted $SRC -> $PDF and $PDF_DARK"
done
