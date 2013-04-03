#!/bin/sh
#create.sh

pygmentize -f latex -O full test.py > test.tex
pygmentize -f latex -O full mocks.py > mocks.tex
xelatex hh-sites-common-tests.tex
