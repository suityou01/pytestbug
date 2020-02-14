#!/usr/bin/env python3
import pytest

@pytest.fixture()
def shared_fixture():
    return "From shared fixture"

#This next line is not possible and gives the following error
#def pytest_runtest_setup(shared_fixture):
'''
Traceback (most recent call last):
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 459, in _importconftest
    return self._conftestpath2mod[key]
KeyError: PosixPath('/home/charlie/pytestbug/tests/conftest.py')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/charlie/pytestbug/venv/bin/pytest", line 8, in <module>
    sys.exit(main())
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 73, in main
    config = _prepareconfig(args, plugins)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 224, in _prepareconfig
    pluginmanager=pluginmanager, args=args
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/hooks.py", line 286, in __call__
    return self._hookexec(self, self.get_hookimpls(), kwargs)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/manager.py", line 93, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/manager.py", line 87, in <lambda>
    firstresult=hook.spec.opts.get("firstresult") if hook.spec else False,
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/callers.py", line 203, in _multicall
    gen.send(outcome)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/helpconfig.py", line 89, in pytest_cmdline_parse
    config = outcome.get_result()
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/callers.py", line 80, in get_result
    raise ex[1].with_traceback(ex[2])
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/callers.py", line 187, in _multicall
    res = hook_impl.function(*args)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 794, in pytest_cmdline_parse
    self.parse(args)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 1000, in parse
    self._preparse(args, addopts=addopts)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 958, in _preparse
    early_config=self, args=args, parser=self._parser
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/hooks.py", line 286, in __call__
    return self._hookexec(self, self.get_hookimpls(), kwargs)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/manager.py", line 93, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/manager.py", line 87, in <lambda>
    firstresult=hook.spec.opts.get("firstresult") if hook.spec else False,
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/callers.py", line 208, in _multicall
    return outcome.get_result()
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/callers.py", line 80, in get_result
    raise ex[1].with_traceback(ex[2])
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/callers.py", line 187, in _multicall
    res = hook_impl.function(*args)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 857, in pytest_load_initial_conftests
    self.pluginmanager._set_initial_conftests(early_config.known_args_namespace)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 405, in _set_initial_conftests
    self._try_load_conftest(anchor)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 411, in _try_load_conftest
    self._getconftestmodules(anchor)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 437, in _getconftestmodules
    mod = self._importconftest(conftestpath)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 484, in _importconftest
    self.consider_conftest(mod)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 537, in consider_conftest
    self.register(conftestmodule, name=conftestmodule.__file__)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/_pytest/config/__init__.py", line 343, in register
    ret = super().register(plugin, name)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/manager.py", line 126, in register
    self._verify_hook(hook, hookimpl)
  File "/home/charlie/pytestbug/venv/lib/python3.6/site-packages/pluggy/manager.py", line 261, in _verify_hook
    notinspec,
pluggy.manager.PluginValidationError: Plugin '/home/charlie/pytestbug/tests/conftest.py' for hook 'pytest_runtest_setup'
hookimpl definition: pytest_runtest_setup(shared_fixture)
Argument(s) {'shared_fixture'} are declared in the hookimpl but can not be found in the hookspec
'''
def pytest_runtest_setup():    
    print("From pytest_runtest_setup")
    # This next line prints <function shared_fixture at 0x7fa549696620> which is the function pointer rather than the result
    print(shared_fixture)
    # This next line is what causes the problem I reported, except that the error message is the bug
    # In that it reports incorrectly that the issue with calling the fixture incorrectly occurs in the 2 test methods in tests.py which is not the case
    s=shared_fixture() # <<<<< The error should point to this line
    print(s)
    
'''
====================================================================== test session starts ======================================================================
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/charlie/pytestbug
collected 2 items                                                                                                                                               

tests/tests.py EE                                                                                                                                         [100%]

============================================================================ ERRORS =============================================================================
_____________________________________________________________ ERROR at setup of TestSuite.test_one ______________________________________________________________

    def pytest_runtest_setup():
        print("From pytest_runtest_setup")
        print(shared_fixture)
>       assert 0
E       assert 0

tests/conftest.py:82: AssertionError
--------------------------------------------------------------------- Captured stdout setup ---------------------------------------------------------------------
From pytest_runtest_setup
<function shared_fixture at 0x7fa549696620>
_____________________________________________________________ ERROR at setup of TestSuite.test_two ______________________________________________________________

    def pytest_runtest_setup():
        print("From pytest_runtest_setup")
        print(shared_fixture)
>       assert 0
E       assert 0

tests/conftest.py:82: AssertionError
--------------------------------------------------------------------- Captured stdout setup ---------------------------------------------------------------------
From pytest_runtest_setup
<function shared_fixture at 0x7fa549696620>
======================================================================= 2 errors in 0.04s =======================================================================
(venv) charlie@locke:~/pytestbug$ pytest tests/*.py
====================================================================== test session starts ======================================================================
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/charlie/pytestbug
collected 2 items                                                                                                                                               

tests/tests.py EE                                                                                                                                         [100%]

============================================================================ ERRORS =============================================================================
_____________________________________________________________ ERROR at setup of TestSuite.test_one ______________________________________________________________
Fixture "shared_fixture" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/latest/fixture.html for more information about fixtures, and
https://docs.pytest.org/en/latest/deprecations.html#calling-fixtures-directly about how to update your code.
--------------------------------------------------------------------- Captured stdout setup ---------------------------------------------------------------------
From pytest_runtest_setup
<function shared_fixture at 0x7f26044b5620>
_____________________________________________________________ ERROR at setup of TestSuite.test_two ______________________________________________________________
Fixture "shared_fixture" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/latest/fixture.html for more information about fixtures, and
https://docs.pytest.org/en/latest/deprecations.html#calling-fixtures-directly about how to update your code.
--------------------------------------------------------------------- Captured stdout setup ---------------------------------------------------------------------
From pytest_runtest_setup
<function shared_fixture at 0x7f26044b5620>
======================================================================= 2 errors in 0.01s =======================================================================
'''