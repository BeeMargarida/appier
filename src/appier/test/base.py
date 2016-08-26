#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (c) 2008-2016 Hive Solutions Lda.
#
# This file is part of Hive Appier Framework.
#
# Hive Appier Framework is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Appier Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Appier Framework. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import unittest

import appier

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.app = appier.App()

    def tearDown(self):
        self.app.unload()

    def test_locale(self):
        self.app.locales = ("en_us", "pt_pt", "es_es")
        self.app._register_bundle(dict(hello = "Hello"), "en_us")
        self.app._register_bundle(dict(hello = "Olá"), "pt_pt")

        result = self.app.to_locale("hello")
        self.assertEqual(result, "Hello")

        result = self.app.to_locale("hello", locale = "en_us")
        self.assertEqual(result, "Hello")

        result = self.app.to_locale("hello", locale = "en-us")
        self.assertEqual(result, "Hello")

        result = self.app.to_locale("hello", locale = "pt_pt")
        self.assertEqual(result, "Olá")

        result = self.app.to_locale("hello", locale = "pt-pt")
        self.assertNotEqual(result, "Olá")
        self.assertEqual(result, "Hello")

        result = self.app.to_locale("hello", locale = "es_es")
        self.assertNotEqual(result, "Hola")
        self.assertEqual(result, "Hello")

        self.app._register_bundle(dict(hello = "Hola"), "es_es")

        result = self.app.to_locale("hello", locale = "es_es")
        self.assertEqual(result, "Hola")

        result = self.app.to_locale("hello", locale = "en")
        self.assertEqual(result, "Hello")

        result = self.app.to_locale("hello", locale = "pt")
        self.assertEqual(result, "Olá")

        result = self.app.to_locale("hello", locale = "es")
        self.assertEqual(result, "Hola")

        result = self.app.to_locale("bye")
        self.assertEqual(result, "bye")

        result = self.app.to_locale("bye", locale = "cn")
        self.assertEqual(result, "bye")

        self.app._register_bundle(dict(bye = "Bye"), "en_us")

        result = self.app.to_locale("bye")
        self.assertEqual(result, "Bye")

        result = self.app.to_locale("bye", locale = "en_us")
        self.assertEqual(result, "Bye")

        result = self.app.to_locale("bye", locale = "pt_pt")
        self.assertEqual(result, "Bye")

        result = self.app.to_locale("bye", locale = "pt_pt", fallback = False)
        self.assertEqual(result, "bye")

    def test_slugify(self):
        if not self.app.slugify:
            if not hasattr(self, "skipTest"): return
            self.skipTest("No slugify engine present")

        result = self.app.slugify_slugify("hello world")
        self.assertEqual(result, "hello-world")

        result = self.app.slugify_slugify("你好世界")
        self.assertEqual(result, "ni-hao-shi-jie")

    def test_slugier(self):
        if not self.app.slugier:
            if not hasattr(self, "skipTest"): return
            self.skipTest("No slugier engine present")

        result = self.app.slugify_slugier("hello world")
        self.assertEqual(result, "hello-world")

        result = self.app.slugify_slugier("olá mundo")
        self.assertEqual(result, "ola-mundo")

        result = self.app.slugify_slugier("你好世界")
        self.assertEqual(result, "%e4%bd%a0%e5%a5%bd%e4%b8%96%e7%95%8c")
