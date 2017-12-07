from pytest import fixture


@fixture
def bad_py_text():
    return ['import os, sys\n', '\n', '\n',
            'def SomeInvalidName():\n', '    pass\n']


@fixture
def good_py_text():
    return ['"""\n', 'A good py\n',
            '"""\n', '\n', '\n', 'def foobar():\n',
            '    """This is a function"""\n',
            "    return 'bar'\n"]


@fixture
def good_py_file(tmpdir, good_py_text):
    py_file = tmpdir.mkdir('dummy').join('good.py')
    py_file.write(''.join(good_py_text))
    return py_file


@fixture
def bad_py_file(tmpdir, bad_py_text):
    py_file = tmpdir.mkdir('dummy').join('bad.py')
    py_file.write(''.join(bad_py_text))
    return py_file
