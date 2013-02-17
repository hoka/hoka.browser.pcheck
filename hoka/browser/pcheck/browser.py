from hoka.browser.base import *
from AccessControl import Unauthorized
from AccessControl.SecurityManagement import getSecurityManager
from AccessControl.Permission import _registeredPermissions

"""
dummy all methods are generated
every permission you can see in permission tab in controlpannel is
placed here as method
can_PERMISSION NAME returns True or False
auth_PERMISSION NAME raises unauthorized if user hasn't the permission
"""

GENERATED=False

class IPCheck(Interface):

    def raise_anon(self):
        """ """

class Browser(BrowserView):

    implements(IPCheck)

    def _check_permission(self,permission_name):
        return getSecurityManager().checkPermission(permission_name, self.context)

    def _auth(self,permission_name):
        if not self._check_permission(permission_name):
            raise Unauthorized

    def raise_anon(self):

        context=self.context
        if context.get_adapter('auth')().getUserName() == 'Anonymous User':
            raise Unauthorized

    def __init__(self, context, request):
        BrowserView.__init__(self, context, request)
        #first call

        global GENERATED
        if not GENERATED:
            for permission_name in _registeredPermissions.keys():
                method_name=_create_permission_name(permission_name)
                _create_can(permission_name,method_name)
                _create_auth(permission_name,method_name)
                _add_methods()
            GENERATED=True


def _create_can(permission_name,method_name):
    """ """
    method_='''def can_%(method_name)s(self):
            return self._check_permission("""%(permission_name)s""")'''%{'method_name':method_name,
                                                                        'permission_name':permission_name}

    interface_='''def can_%(method_name)s(self):
                    """ """'''%{'method_name':method_name,
                              'permission_name':permission_name}

    exec interface_ in interfaces_
    exec method_ in methods_

def _create_auth(permission_name,method_name):
    """ """
    method_='''def auth_%(method_name)s(self):
            self._auth("""%(permission_name)s""")'''%{'method_name':method_name,
                                                          'permission_name':permission_name}

    interface_='''def auth_%(method_name)s(self):
                    """ """'''%{'method_name':method_name,
                              'permission_name':permission_name}

    exec interface_ in interfaces_
    exec method_ in methods_


def _create_permission_name(string_):
    """ """
    string_=string_.lower()
    string_=string_.replace(':','')
    string_=string_.replace(' ','_')
    string_=string_.replace('.','_')
    string_=string_.replace(',','_')
    string_=string_.replace('/','_')
    string_=string_.replace('-','_')
    string_=string_.replace("'",'')

    return string_

interfaces_={}
methods_={}
def _add_methods():
    """ """
    for k,v in methods_.items():
        setattr(Browser,k,v)

    for k,v in interfaces_.items():

        setattr(IPCheck,k,v)
