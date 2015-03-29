#!/usr/bin/env python
# (C) 2008-2015 Michael 'Mickey' Lauer <mickey@vanille.de>
# GPLv3

"""
This program converts documented dbus-xml files to markdown.
"""

import sys
import xml.sax
from xml.sax.handler import ContentHandler

##############################################################################
class Entity(object):
##############################################################################

    def __init__(self, name, attrs=None):
        print("creating entity: ", self.__class__.__name__, name)
        self.name = name
        self.attrs = attrs
        self.title = "Untitled"

    def output(self):
        pass

    def out(self):
        return ""

    def outputSectionHeader(self, content, size=1):
        return "\n%s%s\n" % ( "#" * size, content )

    def outputParagraph(self, content):
        return "\n%s\n" % (content)

    def outputTypewriter(self, content):
        return "```%s```" % (content)

    def outputAnchorLink(self, content):
        return """[%s](%s)""" % ( content, content )

    def outputAnchorLabel(self, content):
        return """<a name="%s">%s</a>""" % ( content, content )

    def outputCrosslinked(self, content):
        result = ""
        for word in content.split(' '):
            if word.startswith("org.freesmartphone"):
                word = word.strip(",./:;()")
                dotted = word.split('.')
                html, method = '.'.join(dotted[:-1]), dotted[-1]
                print("possible link to %s.%s detected" % ( html, method ) )
                result += """<a href="specs/%s/#%s">%s</a>""" % ( html, method, method)
            else:
                result += word
            result += " "
        return result

    def outputDescription(self, content):
        # check for crosslinks
        result = "**Description:** "
        result += self.outputCrosslinked(content)
        return result

    def outputImplementationNote(self, content):
        return """***Implementation Note***\n%s\n""" % self.outputSemiFormatted( content )

    def outputSemiFormatted(self, content):
        content = self.outputCrosslinked(content)
        """convert known html entities"""
        for i in "ul ol li p".split():
            content = content.replace("[%s]" % i, "<%s>" % i)
            content = content.replace("[/%s]" % i, "</%s>" % i)
        return """\n%s\n""" % content

    def outputList(self, entries):

        if not len(entries):
            return "*None*\n"

        else:
            t = "\n"
            for entry in entries:
                t += "* %s\n" % entry
            t += "\n"
            return t

    def outputHeader(self, cssfile=None):
        return \
            """
# freesmartphone.org: %s
            """ % ( self.title )

    def outputFooter(self):
        return \
            """the footer here"""

##############################################################################
class Interface(Entity):
##############################################################################

    def __init__(self, filename):
        Entity.__init__(self, None, None)

        self.filename = filename
        self.methods = []
        self.signals = []
        self.properties = []
        self.errors = []
        self.outfile = None
        self.namespace = "Unknown"
        self.description = "Unknown"

    def output(self):
        import os.path
        basename = os.path.basename(self.filename).replace(".xml.in", ".md")
        # dirname = os.path.dirname(__file__)
        self.outfilename = "./docs/specs/%s" % (basename)
        self.outfile = open(self.outfilename, "w")

        text = self.outputHeader(__file__.replace("makedoc.py", "style.xml"))
        text += "\n"

        text += self.outputSectionHeader(self.namespace)

        # description
        text += self.outputSectionHeader("Description", 2)
        text += "\n"
        text += self.outputParagraph(self.description)
        text += "\n"

        # namespace
        text += self.outputSectionHeader("Namespace", 2)
        text += "\n"
        text += self.outputParagraph(self.outputTypewriter(self.namespace))
        text += "\n"

        # method overview
        text += self.outputSectionHeader("Methods", 2)
        text += self.outputList([self.outputAnchorLink(method.name)
                                 for method in self.methods])

        # signal overview
        text += self.outputSectionHeader("Signals", 2)
        text += self.outputList([self.outputAnchorLink(signal.name)
                                 for signal in self.signals])

        # property overview
        text += self.outputSectionHeader("Properties", 2)
        text += self.outputList([self.outputAnchorLink(prop.name)
                                 for prop in self.properties])

        # error overview
        text += self.outputSectionHeader("Errors", 2)
        text += self.outputList([self.outputAnchorLink(error.name)
                                 for error in self.errors])

        # methods en detail
        if len(self.methods):
            text += self.outputSectionHeader("Methods")
            for m in self.methods:
                text += m.out()

        # signals en detail
        if len(self.signals):
            text += self.outputSectionHeader("Signals")
            for s in self.signals:
                text += s.out()

        # properties en detail
        if len(self.properties):
            text += self.outputSectionHeader("Properties")
            for s in self.properties:
                text += s.out()

        # errors en detail
        if len(self.errors):
            text += self.outputSectionHeader("Errors")
            for e in self.errors:
                text += e.out()

        text += self.outputFooter()
        text += "\n"

        assert self.outfile is not None
        self.outfile.write(text)

##############################################################################
class Describable(Entity):
##############################################################################

    def __init__(self, name, attrs):
        Entity.__init__(self, name, attrs)
        self.description = None
        self.inote = None

    def describe(self):
        text = ""
        if self.description is not None:
            text += self.outputParagraph(
                self.outputDescription(self.description))
        if self.inote is not None:
            text += self.outputParagraph(
                self.outputImplementationNote(self.inote))
        return text

    def __repr__(self):
        return "<Describable:%s>" % self.name

##############################################################################
class Method(Describable):
##############################################################################

    def __init__(self, name, attrs):
        Describable.__init__(self, name, attrs)
        self.args = []

    def signature(self):
        outparam = ""
        inparam = ""
        try:
            for arg in self.args:
                if arg.attrs["direction"] == "in":
                    inparam += arg.attrs["type"]
                elif arg.attrs["direction"] == "out":
                    outparam += arg.attrs["type"]
                else:
                    raise KeyError("Direction neither 'in' nor 'out'")
        except KeyError as e:
            print >>sys.stderr, "[ERROR] Invalid signature for method", self, e
            sys.exit(-1)
        return inparam, outparam

    def out(self):
        text = ""
        inparam, outparam = self.signature()
        if inparam and outparam:
            text += "%s ( %s ) &rarr; %s" % (self.outputAnchorLabel(self.name),
                                             inparam, outparam)
            text = self.outputSectionHeader(text, 3)
            text += "\n"
            text += self.describe()
            text += self.inparam()
            text += self.outparam()
        elif inparam and not outparam:
            text += "%s ( %s )" % (self.outputAnchorLabel(self.name), inparam)
            text = self.outputSectionHeader(text, 3)
            text += "\n"
            text += self.describe()
            text += self.inparam()
        elif not inparam and outparam:
            text += "%s ( ) &rarr; %s" % (self.outputAnchorLabel(self.name),
                                          outparam)
            text = self.outputSectionHeader(text, 3)
            text += "\n"
            text += self.describe()
            text += self.outparam()
        else:
            text += "%s ( )" % (self.outputAnchorLabel(self.name))
            text = self.outputSectionHeader(text, 3)
            text += self.describe()

        text += "\n"

        return text

    def inparam(self):
        text = self.outputSectionHeader("Parameters", 4)
        for arg in self.args:
            if arg.attrs["direction"] == "in":
                text += arg.out()
        return text

    def outparam(self):
        text = self.outputSectionHeader("Returns", 4)
        for arg in self.args:
            if arg.attrs["direction"] == "out":
                text += arg.out()
        return text

##############################################################################
class Signal(Describable):
##############################################################################

    def __init__(self, name, attrs):
        Describable.__init__(self, name, attrs)
        self.args = []

    def signature(self):
        param = ""
        for arg in self.args:
            param += arg.attrs["type"]
        return param

    def out(self):
        text = ""
        param = self.signature()
        if param:
            text += "%s ( %s )" % (self.outputAnchorLabel(self.name), param)
            text = self.outputSectionHeader(text, 3)
            text += self.describe()
            text += self.param()
        else:
            text += "%s ( )" % (self.outputAnchorLabel(self.name))

        text = self.outputSectionHeader(text, 3)
        text += "\n"

        return text

    def param(self):
        text = self.outputSectionHeader("Parameters", 4)
        for arg in self.args:
            text += arg.out()
        return text

##############################################################################
class Property(Describable):
##############################################################################

    def __init__(self, name, attrs):
        Describable.__init__(self, name, attrs)

    def out(self):
        text = ""

        accesstype = "Read/Write"
        if "access" in self.attrs and self.attrs["access"] == "readonly":
            accesstype = "Read only"

        typename = self.attrs["type"]
        text += "%s - %s : %s" % (self.outputAnchorLabel(self.name),
                                  typename, accesstype)
        text = self.outputSectionHeader(text, 3)
        text += self.outputSemiFormatted(self.describe())

        text = self.outputSectionHeader(text, 3)
        text += "\n"

        return text

##############################################################################
class Error(Describable):
##############################################################################

    def __init__(self, name, attrs):
        Describable.__init__(self, name, attrs)

    def out(self):
        text = ""
        text += "%s" % (self.outputAnchorLabel(self.name))
        text = self.outputSectionHeader(text, 3)
        text += self.describe()
        text += "\n"

        return text

##############################################################################
class Argument(Entity):
##############################################################################

    def __init__(self, name, attrs):
        Entity.__init__(self, name, attrs)
        self.docs = ""

    def out(self):
        t = self.attrs.get("type", "Unknown Type")
        n = self.attrs.get("name", "Unknown Name")

        text = ""
        text += "<i>%s: %s</i>%s\n" % (t, n, self.outputSemiFormatted(self.docs))
        return text

##############################################################################
class Handler(ContentHandler):
##############################################################################

    def __init__(self, iface):
        ContentHandler.__init__(self)
        self.iface = iface
        self.parent = None
        self.current = None
        self.doc = None
        self.method = None
        self.signal = None
        self.property = None
        self.error = None
        self.arg = None
        self.text = ""
        self.significantElements = "node interface method signal error arg property".split()

    def startDocument(self):
        pass

    def endDocument(self):
        pass

    def startElement(self, element, attrs):
        if element in self.significantElements:
            print("--- setting current element to ", element)
            self.current = element
        if element.startswith("doc:"):
            self.doc = element.split(':')[1]
        self.name = attrs.get("name", "")
        self.attrs = attrs
        print(element, self.name, "(in %s)" % self.current or None)

        if element == "interface":
            self.iface.namespace = self.name.strip()

        elif element == "method":
            self.method = Method(self.name.strip(), attrs)

        elif element == "arg":
            self.arg = Argument(self.name.strip(), attrs)

        elif element == "signal":
            self.signal = Signal(self.name.strip(), attrs)

        elif element == "property":
            self.property = Property(self.name.strip(), attrs)

        elif element == "error":
            self.error = Error(self.name.strip(), attrs)

    def characters(self, char):
        c = char.strip() + " "
        if c:
            # print c
            self.text += c

    def endElement(self, element):

        if element == "doc:summary" and self.current == "node":
            self.iface.title = self.text.strip()

        elif element == "doc:summary" and self.current == "arg":
            self.arg.docs = self.text.strip()

        elif element == "doc:para" and self.current == "interface":
            self.iface.description = self.text.strip()

        elif element == "doc:description" and self.current == "method":
            self.method.description = self.text.strip()

        elif element == "doc:description" and self.current == "signal":
            self.signal.description = self.text.strip()

        elif element == "doc:description" and self.current == "property":
            self.property.description = self.text.strip()

        elif element == "doc:description" and self.current == "error":
            self.error.description = self.text.strip()

        elif element == "doc:inote" and self.current == "method":
            self.method.inote = self.text.strip()

        elif element == "method":
            assert self.method is not None
            self.iface.methods.append(self.method)
            self.method = None

        elif element == "signal":
            assert self.signal is not None
            self.iface.signals.append(self.signal)
            self.signal = None

        elif element == "property":
            assert self.property is not None
            self.iface.properties.append(self.property)
            self.signal = None

        elif element == "error":
            assert self.error is not None
            self.iface.errors.append(self.error)
            self.error = None

        elif element == "arg":
            assert self.arg is not None
            if self.method is not None:
                self.method.args.append(self.arg)
            else:
                self.signal.args.append(self.arg)
            self.arg = None

        print(repr(self.text), repr(element))

        self.text = ""
        if element in self.significantElements:
            print("resetting current element")
            self.current = None
            self.parent = element

##############################################################################
if __name__ == "__main__":
##############################################################################
    print("parsing...")
    interfaces = []
    for filename in sys.argv[1:]:
        interface = Interface(filename)
        interfaces.append(interface)
        handler = Handler(interface)
        xml.sax.parse(filename, handler)
    print("creating...")
    for iface in interfaces:
        iface.output()
