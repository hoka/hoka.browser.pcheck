import unittest
from OFS.Application import Application
from zope.configuration import xmlconfig

import hoka.browser.pcheck
import hoka.adapter.auth


import zope.component
import z3c.autoinclude
context = xmlconfig.file('meta.zcml', zope.component)
xmlconfig.file('meta.zcml', z3c.autoinclude, context=context)
xmlconfig.file('configure.zcml', hoka.browser.pcheck, context=context)
xmlconfig.file('configure.zcml', hoka.adapter.auth, context=context)


def makeConnection():
    import ZODB
    from ZODB.DemoStorage import DemoStorage

    s = DemoStorage()
    return ZODB.DB( s ).open()

class TestBase(unittest.TestCase):

    def setUp( self ):
        self.connection = makeConnection()
        r = self.connection.root()
        a = Application()
        r['Application'] = a
        self.root = a

    def test_pcheck(self):
        browserview=hoka.browser.pcheck.browser.Browser(self.root,object())
        self.assertEqual(browserview.can_view(), 1 )
        browserview.auth_view()
        try:
            browserview.raise_anon()
        except Exception,e:
            self.assertEqual(str(e),'Unauthorized()')

if __name__ == '__main__':
    unittest.main()
