AC_INIT([freesmartphone.github.io], [0.5], [fso@openphoenux.org], [freesmartphone.github.io])
AC_CONFIG_SRCDIR([Makefile.am])
AM_INIT_AUTOMAKE([dist-bzip2])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AM_PATH_PYTHON([3.1])

MKDOCS_REQUIRED=0.11.1
AC_PATH_PROG(MKDOCS, mkdocs, mkdocs)
AC_SUBST(MKDOCS)
m4_ifdef([AM_PROG_MKDOCS], [AM_PROG_MKDOCS([$VALA_REQUIRED])])

FSO_SPECS_REQUIRED=2012.01.01

PKG_CHECK_MODULES(FSO_SPECS,
        fso-specs >= $FSO_SPECS_REQUIRED,
	[FSO_SPECS_DATADIR=`$PKG_CONFIG --variable=pkgdatadir fso-specs`]
)

AC_SUBST(FSO_SPECS_DATADIR)

AC_SUBST(FSO_SPECS_CFLAGS)
AC_SUBST(FSO_SPECS_LIBS)

AC_CONFIG_FILES([
        Makefile
])
AC_OUTPUT
