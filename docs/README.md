Generate reStructuredText:
```
$ pandoc -s -t rst --toc README.md -o docs/README.rst
```

Generate HTML:
```
$ pandoc -s --toc -c pandoc.css README.md -o docs/index.html
```

