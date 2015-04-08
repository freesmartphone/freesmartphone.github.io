DBUS_DOCFILES = $(wildcard $(FSO_SPECS_DATADIR)/doc/*/*.in)
DBUS_MDFILES = $(patsubst %.xml.in,%.md,$(DBUS_DOCFILES))

handwritten: tools/makedoc.py mkdocs.yml $(wildcard docs/*.md)
	$(MKDOCS) build	--clean

generated: tools/makedoc.py $(DBUS_MDFILES)

all: generated handwritten

test: generated handwritten
	killall `basename $(MKDOCS)` || true
	$(MKDOCS) serve

%.md: %.xml.in
	tools/makedoc.py $<

MAINTAINERCLEANFILES = \
  aclocal.m4 compile config.guess config.sub \
  configure depcomp install-sh ltmain.sh     \
  Makefile.in missing config.h.in            \
  mkinstalldirs \
  src/*.h src/*.c .deps
