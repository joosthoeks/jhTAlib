#!/bin/sh
pandoc -s -t html5 --toc -c pandoc.css README.md -o docs/index.html
pandoc -s -t epub --toc README.md -o docs/README.epub
pandoc -s -t json --toc README.md -o docs/README.json
pandoc -s -t odt --toc README.md -o docs/README.odt
pandoc -s -t latex --toc README.md -o docs/README.pdf
#pandoc -s -t rst --toc README.md -o docs/README.rst
#pandoc -s -t rtf --toc README.md -o docs/README.rtf
pandoc -s -t opendocument --toc README.md -o docs/README.xml

