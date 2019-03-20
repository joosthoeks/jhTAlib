Generate HTML5:

```
$ pandoc -s -t html5 --toc -c pandoc.css README.md -o docs/index.html
```

Generate EPUB ebook:

```
$ pandoc -s -t epub --toc README.md -o docs/README.epub
```

Generate JSON:

```
$ pandoc -s -t json --toc README.md -o docs/README.json
```

Generate ODT (OpenDocument Text, readable by LibreOffice):

```
$ pandoc -s -t odt --toc README.md -o docs/README.odt
```

Generate PDF:

```
$ pandoc -s -t latex --toc README.md -o docs/README.pdf
```

Generate reStructuredText:

```
$ pandoc -s -t rst --toc README.md -o docs/README.rst
```

Generate Rich text format (RTF):

```
$ pandoc -s -t rtf --toc README.md -o docs/README.rtf
```

Generate OpenDocument XML:

```
$ pandoc -s -t opendocument --toc README.md -o docs/README.xml
```

