#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: wikiseriessjoerdlib.py
#
# Copyright 2023 Sjoerd van den Bos
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.
#

"""
Main code for wikiseriessjoerdlib.

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html

"""

import logging

__author__ = '''Sjoerd van den Bos <test@example.com>'''
__docformat__ = '''google'''
__date__ = '''26-04-2023'''
__copyright__ = '''Copyright 2023, Sjoerd van den Bos'''
__credits__ = ["Sjoerd van den Bos"]
__license__ = '''MIT'''
__maintainer__ = '''Sjoerd van den Bos'''
__email__ = '''<test@example.com>'''
__status__ = '''Development'''  # "Prototype", "Development", "Production".


# This is the main prefix used for logging
LOGGER_BASENAME = '''wikiseriessjoerdlib'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.addHandler(logging.NullHandler())