DBUS_DOCFILES = $(wildcard $(FSO_SPECS_DATADIR)/doc/*/*.in)
DBUS_MDFILES = $(patsubst %.xml.in,%.md,$(DBUS_DOCFILES))

handwritten: mkdocs.yml $(wildcard docs/*.md) docs/specs/intro.md
	$(MKDOCS) --clean build	

generated: $(DBUS_MDFILES)

all: generated handwritten

%.md: %.xml.in
	tools/makedoc.py $<

MAINTAINERCLEANFILES = \
  aclocal.m4 compile config.guess config.sub \
  configure depcomp install-sh ltmain.sh     \
  Makefile.in missing config.h.in            \
  mkinstalldirs \
  src/*.h src/*.c .deps
