#openAnything

import urllib
import StringIO
from xml.dom import minidom

def openAnything(source):
    """try to open any data source and return a file-like object"""
    
    # try to open with urllib (if source is http, ftp, or file URL
    try:
        return urllib.urlopen(source)
    except (IOError, OSError):
        pass
    
    # try to open with native open function (if source is pathname)
    try:
        return open(source)
    except (IOError, OSError):
        pass
    
    # treat source as string
    return StringIO.StringIO(str(source))

def fileLike(forXML):
    """convert to a file like object and print"""
    xmldoc = minidom.parse(forXML)
    print xmldoc.toxml()
    print "\n------------\n"

source1 = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"
source2 = 'http://slashdot.org/slashdot.rdf'
source3 = 'binary.xml'

sourceList = (source1, source2, source3)

for source in sourceList:
    fileLike(openAnything(source))
