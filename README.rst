Introduction
============

Browser to validate user permission. Every permission which
is defined in zope is mapped to a cleaned up generated method.
The Example is for the defined permission "myproject.manage_function"

can_PERMISSION NAME returns True or False
auth_PERMISSION NAME raises unauthorized if user hasn't the permission

The permissions avaliable are the Permissions you can see unter Manage Access im ZMI

Example::

    context.get_browser('pcheck').can_myproject_manage_function()
    context.get_browser('pcheck').auth_myproject_manage_function()
