all:
	pdflatex main
	bibtex main
	-bibtex web
	bibtex mine
	pdflatex main
	pdflatex main

clean:
	rm -f *.aux *.bbl *.lbl *.loa *.loe *.lof *.log *.maf *.mlf* *.mlt* *.mtc* *.toc *.blg
