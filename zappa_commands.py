"""
Be in no doubt: this is a hack.

But why?

Well. AWS Lambda can 'invoke' functions directly or from a schedule. See
`events` in zappa_settings.json for more on them.

The problem is that django's management commands aren't exposed as functions,
they are intended to be run from the command line as an argument to
`manage.py`.

Also, invoke is meant to be passed a path to a callable that's then called.

This magic does a few things:

1. Turn the whole module in to a class. This is not recommended in normal use,
   so don't get any ideas. This is what `sys.modules[__name__] = Runner()`
   is doing.

2. Overwrite `__getattr__` on the class. This is also not recommended in normal
   use. Remember this is now `__getattr__` on the *file* because the file is
   the class.

3. For any attr, return a python lambda that when called will return a
   function that can be called by AWS Lambda.

Due to AWS Lambda limitations, you can't pass arguments to the command at all.

Note: this is only intended for scheduled tasks. For running management
commands you should use `zappa manage`.
"""

class Runner:
    def __getattr__(self, attr):
        from django.core.management import call_command
        return lambda: call_command(attr)

import sys
sys.modules[__name__] = Runner()
