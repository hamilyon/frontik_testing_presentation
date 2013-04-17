#!/bin/sh
#create.sh

#pdfcrop interconnection.pdf interconnection.pdf
#pdfcrop frontikarchitecture.pdf frontikarchitecture.pdf

pygmentize -f latex -O full test.py > test.tex
grep -v usepackage test.tex  | grep -v document | grep -v documentclass > test2.tex

pygmentize -f latex -O full mocks.py > mocks.tex
grep -v usepackage mocks.tex  | grep -v document | grep -v documentclass mocks.tex

xelatex -shell-escape logic_tests.tex
