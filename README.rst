Proofreader Python
==================

proofreader-python is a tool for enforcing opinionated coding standards
and conventions through static analysis of the code.

It uses:

- `Pylint`_
- `Flake8`_

Dependencies
------------

-  Python 2.7
-  Python >=3.5

Installation
------------

``pip install proofreader`` \*\* not yet implemented \*\*

or

``python setup.py install``

Usage
-----

``python -m proofreader [targets]`` targets: being paths to python files
or packages seperated by spaces

Configuration
-------------

``proofreader`` contains a default configuration files for both
`pylint`_ and `flake8`_ these can be found in ``proofreader.config``
these can be overridden by providing your own configuration files in the
root directory you run the ``proofreader`` module from.

Testing
=======

You can run the full automated test suite from the base folder with:

``$ ./project_tests.sh``

.. _Pylint: https://github.com/PyCQA/pylint
.. _Flake8: https://github.com/PyCQA/flake8
.. _pylint: https://github.com/PyCQA/pylint
.. _flake8: https://github.com/PyCQA/flake8
