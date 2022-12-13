INSTALL = .
BUILDDIR = ./build
IMGDIR = img

all: $(BUILDDIR)/web.html $(BUILDDIR)/cv.pdf

$(BUILDDIR)/web.html: info/* web.template
	python3 $(INSTALL)/parser.py web.template $(BUILDDIR)
	cp -r img $(BUILDDIR)/img # comment out this line if building in-place

$(BUILDDIR)/cv.pdf: info/* cv.template
	python3 $(INSTALL)/parser.py cv.template $(BUILDDIR)
