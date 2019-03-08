Generate HTML5:
```
$ pandoc -s -t html5 --toc -c pandoc.css README.md -o docs/index.html
```

Generate reStructuredText:
```
$ pandoc -s -t rst --toc README.md -o docs/README.rst
```

Generate PDF:
```
$ pandoc -s -t latex --toc README.md -o docs/README.pdf
```

