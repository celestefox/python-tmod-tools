========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-tmod-tools/badge/?style=flat
    :target: https://readthedocs.org/projects/python-tmod-tools
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/mystfox/python-tmod-tools.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/mystfox/python-tmod-tools

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/mystfox/python-tmod-tools?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/mystfox/python-tmod-tools

.. |requires| image:: https://requires.io/github/mystfox/python-tmod-tools/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/mystfox/python-tmod-tools/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/mystfox/python-tmod-tools/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/mystfox/python-tmod-tools

.. |version| image:: https://img.shields.io/pypi/v/tmod.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/tmod

.. |commits-since| image:: https://img.shields.io/github/commits-since/mystfox/python-tmod-tools/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/mystfox/python-tmod-tools/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/tmod.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/tmod

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tmod.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tmod

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tmod.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/tmod


.. end-badges

A tool to work with tModLoader .tmod files.

* Free software: ISC license

Installation
============

::

    pip install tmod

Documentation
=============

https://python-tmod-tools.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
