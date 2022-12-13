INSTALL = .
BUILDDIR = ./build
IMGDIR = img

all: $(BUILDDIR)/web.html $(BUILDDIR)/cv.pdf $(BUILDDIR)/resume.pdf

$(BUILDDIR)/web.html: info/* web.template
	python3 $(INSTALL)/parser.py web.template $(BUILDDIR)
	cp -r img $(BUILDDIR)/img # comment out this line if building in-place

$(BUILDDIR)/cv.pdf: info/* cv.template
	python3 $(INSTALL)/parser.py cv.template $(BUILDDIR)

$(BUILDDIR)/resume.pdf: info/* resume.template
	python3 $(INSTALL)/parser.py resume.template $(BUILDDIR)

clean:
	rm -f $(BUILDDIR)/*.log $(BUILDDIR)/*.out $(BUILDDIR)/*.aux $(BUILDDIR)/timeline.svg
	rm -f $(BUILDDIR)/web.html $(BUILDDIR)/cv.pdf $(BUILDDIR)/resume.pdf
