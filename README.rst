.. image:: https://img.shields.io/github/v/tag/pi-top/pi-top-Python-SDK
    :target: https://github.com/pi-top/pi-top-Python-SDK/releases
    :alt: GitHub tag (latest by date)

.. image:: https://img.shields.io/github/v/release/pi-top/pi-top-Python-SDK
    :target: https://github.com/pi-top/pi-top-Python-SDK/releases
    :alt: GitHub release (latest by date)

.. image:: https://img.shields.io/pypi/v/pitop
   :target: https://pypi.org/project/pitop
   :alt: PyPI release

.. image:: https://img.shields.io/github/workflow/status/pi-top/pi-top-Python-SDK/Latest%20Build
  :target: https://github.com/pi-top/pi-top-Python-SDK/actions?query=workflow%3A%22Latest+Build%22
  :alt: Latest Build Status

.. image:: https://readthedocs.com/projects/pi-top-pi-top-python-sdk/badge/?version=latest&token=13589f150cf192dcfc6ebfd53aae33164450aafd181c5e49018a21fd93149127
    :target: https://docs.pi-top.com/python-sdk/en/latest/?badge=latest
    :alt: Documentation

.. image:: https://img.shields.io/lgtm/grade/python/g/pi-top/pi-top-Python-SDK.svg
   :target: https://lgtm.com/projects/g/pi-top/pi-top-Python-SDK/context:python
   :alt: Language grade: Python

.. image:: https://img.shields.io/lgtm/grade/javascript/g/pi-top/pi-top-Python-SDK.svg
   :target: https://lgtm.com/projects/g/pi-top/pi-top-Python-SDK/context:javascript
   :alt: Language grade: Javascript

.. image:: https://img.shields.io/codecov/c/gh/pi-top/pi-top-Python-SDK?token=hfbgB9Got4
   :target: https://app.codecov.io/gh/pi-top/pi-top-Python-SDK
   :alt: Codecov

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://results.pre-commit.ci/latest/github/pi-top/pi-top-Python-SDK/master
   :alt: pre-commit.ci status

===========================
pi-top Python SDK (Preview)
===========================

A simple, modular interface for interacting with a pi-top and its related accessories and components.

.. ###############################################
.. # NOTE: THESE ARE EXTERNAL LINKS, AS THEY ARE #
.. # REQUIRED FOR THE IMAGES TO SHOW ON PYPI     #
.. ###############################################

Supports all pi-top devices:

.. image:: https://github.com/pi-top/pi-top-Python-SDK/raw/master/docs/_static/overview/devices.jpg

Supports pi-top Maker Architecture (PMA):

.. image:: https://github.com/pi-top/pi-top-Python-SDK/raw/master/docs/_static/overview/pma.jpg

Supports all pi-top peripherals:

.. image:: https://github.com/pi-top/pi-top-Python-SDK/raw/master/docs/_static/overview/peripherals.jpg

--------------------------
Status: Active Development
--------------------------

This SDK is currently in active development. Please be patient while we work towards v1.0.0!

Backwards Compatibility
=======================

When this library reaches v1.0.0, we will aim to maintain backwards-compatibility thereafter. Until then, every effort will be made to ensure stable support, but it cannot be guaranteed. Breaking changes will be clearly documented.

-----
About
-----

This SDK aims to provide an easy-to-use framework for managing a pi-top. It includes a Python 3 package (`pitop`),
with several modules for interfacing with a range of pi-top devices and peripherals It also contains CLI utilities,
to interact with your pi-top using the terminal.

The SDK is included out-of-the-box with pi-topOS.

Ensure that you keep your system up-to-date to enjoy the latest features and bug fixes.

This library is installed as a Python 3 module called `pitop`. It includes several
submodules that allow you to easily interact with most of the hardware inside a pi-top.

You can easily connect different components of the system using the
modules available in the library:


.. code-block:: python

    from time import sleep
    from pitop import UltrasonicSensor
    from pitop import Pitop

    pitop = Pitop()
    utrasonic = UltrasonicSensor("D1")

    while True:
        pitop.miniscreen.display_text(utrasonic.distance)
        sleep(0.1)

Check out the `API Recipes`_ chapter of the documentation for ideas on how to get started.

.. _API Recipes: https://docs.pi-top.com/python-sdk/en/stable/recipes_api.html


This repository also contains a 'pi-top' command-line interface (CLI) for some SDK functionality:

.. code-block:: bash

    $ pi-top oled write "Hey! I'm a $(pt devices hub)"


A 'pt' alias is also provided for quicker typing:

.. code-block:: bash

    $ pt oled write "Hey! I'm a $(pt devices hub)"

Check out the `CLI`_ chapter of the documentation for ideas on how to get started.

.. _CLI: https://docs.pi-top.com/python-sdk/en/stable/cli_tools.html

------------
Installation
------------

OS
==

The pi-top Python SDK is installed out of the box with pi-topOS, which is available from
pi-top.com_. To install on Raspberry Pi OS or other operating systems, see the `Getting Started`_ chapter.

.. _pi-top.com: https://www.pi-top.com/products/os/
.. _Getting Started: https://docs.pi-top.com/python-sdk/en/stable/getting_started.html


pip
===

The SDK is also available on PyPI.

On ARM devices, such as the Raspberry Pi, you need to include pi-top's repository to meet all the dependencies:

.. code-block:: bash

  pip3 install pitop --extra-index-url=https://packagecloud.io/pi-top/pypi/pypi/simple


On non-ARM devices, you can omit the extra-index-url flag:

.. code-block:: bash

  pip3 install pitop


You can also install a pitop subpackage directly in case you don't need the whole SDK:

.. code-block:: bash

  pip3 install pitop.pma

-------------
Documentation
-------------

Comprehensive documentation is available here_.

.. _here: https://docs.pi-top.com/python-sdk/

------------
Contributing
------------

Please refer to the `Contributing`_ document in this repository
for information on contributing to the project.

.. _Contributing: https://github.com/pi-top/pi-top-Python-SDK/blob/master/.github/CONTRIBUTING.md

See the `contributors page`_ on GitHub for more info on contributors.

.. _contributors page: https://github.com/pi-top/pitop/graphs/contributors
