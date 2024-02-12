PDFLATEX=lualatex -shell-escape -interaction=nonstopmode -halt-on-error

.ONESHELL:

all: pdf/lecture1.pdf
all: pdf/practice1.pdf

pdf/%.pdf: source/%/source.tex source/%/images/*.png
	mkdir -p build/$(@F)
	ls build/$(@F)/images || ln -sv ../../source/$*/images build/$(@F)/images
	cd build/$(@F) && $(PDFLATEX) ../../$< && $(PDFLATEX) ../../$< && mv source.pdf ../../$@

.PHONY: clean
clean:
	rm -rf *.pdf build/*
