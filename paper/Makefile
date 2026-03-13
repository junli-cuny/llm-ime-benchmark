# Produce PS/PDF/DVI files: make
# Clean all output files: make clean

# Use pdflatex or latex
ENGINE=pdflatex

# Name of the master LaTeX file
DOCUMENT=main

#--------------------------------------------------
# Do NOT change anything below
#--------------------------------------------------

default: $(DOCUMENT).pdf

$(DOCUMENT).toc: $(DOCUMENT).tex
	$(ENGINE) $(DOCUMENT).tex

$(DOCUMENT).pdf: $(DOCUMENT).toc
	bibtex $(DOCUMENT);
	bibtex lr;
	$(ENGINE) $(DOCUMENT).tex;
	$(ENGINE) $(DOCUMENT).tex

all: $(DOCUMENT).pdf

clean:
	rm -rf $(DOCUMENT).aux $(DOCUMENT).log $(DOCUMENT).toc \
     $(DOCUMENT).bbl $(DOCUMENT).blg $(DOCUMENT).pdf \
     $(DOCUMENT).ps $(DOCUMENT).dvi $(DOCUMENT).synctex.gz \
	 $(DOCUMENT).fdb_latexmk $(DOCUMENT).fls $(DOCUMENT).out \
	 lr.aux lr.bbl lr.blg \
	 languageresource.aux languageresource.bbl languageresource.blg

open:
	open $(DOCUMENT).pdf
