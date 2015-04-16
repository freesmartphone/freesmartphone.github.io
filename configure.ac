AC_INIT([freesmartphone.github.io], [0.5], [fso@openphoenux.org], [freesmartphone.github.io])
AC_CONFIG_SRCDIR([Makefile.am])
AM_INIT_AUTOMAKE([dist-bzip2])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])

AM_PATH_PYTHON([3.1])

MKDOCS_REQUIRED=0.12.1
AC_CHECK_PROG(MKDOCS_CHECK, mkdocs, yes)
if test x"$MKDOCS_CHECK" != x"yes"; then
    AC_MSG_ERROR([mkdocs is mandatory for this package])
fi
AC_PATH_PROG(MKDOCS,mkdocs)
AC_SUBST(MKDOCS)

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
