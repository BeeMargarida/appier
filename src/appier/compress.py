#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (C) 2008-2015 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import os
import mimetypes

from . import legacy

class Compress(object):

    def __init__(self):
        self._load_compress()

    def load_jsmin(self):
        try: import jsmin
        except: self.jsmin = None; return
        self.jsmin = jsmin

    def type_jpeg(self):
        return "image/jpeg"

    def compress_jpeg(self, file_path):
        if self.jinja:
            return self.compress_jpeg_pil(file_path)

        return self.compress_fallback(file_path)

    def compress_jpeg_pil(self, file_path, quality = 80):
        file = legacy.BytesIO()
        image = self.pil.Image.open(file_path)
        image.save(file, format = "jpeg", quality = quality, optimize = True)
        file.seek(0, os.SEEK_END)
        file_size = file.tell()
        return (file_size, file)

    def compress_js(self, file_path):
        if self.jsmin:
            return self.compress_js_jsmin(file_path)

        return self.compress_fallback(file_path)

    def compress_js_jsmin(self, file_path):
        file = open(file_path, "rb")
        try: data = file.read()
        finally: file.close()
        data = self.jsmin.jsmin(data)
        file_size = len(data)
        file = legacy.BytesIO(data)
        return (file_size, file)

    def compress_fallback(self, file_path):
        size = os.path.getsize(file_path)
        file = open(file_path, "rb")
        return (size, file)

    def _load_compress(self):
        self.load_jsmin()