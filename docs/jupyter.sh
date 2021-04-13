#!/bin/sh
jupyter nbconvert --output-dir=docs --to html --template lab example/*.ipynb
jupyter nbconvert --output-dir=docs --to html --template lab notebook/*.ipynb
