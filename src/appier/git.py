#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (c) 2008-2015 Hive Solutions Lda.
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

from . import util
from . import common

class Git(object):

    @classmethod
    def is_git(cls, path = None):
        path = path or common.base().get_base_path()
        result = util.execute(["git", "status"], path = path)
        code = result["code"]
        return code == 0

    @classmethod
    def get_commit(cls, path = None):
        path = path or common.base().get_base_path()
        result = util.execute(["git", "rev-parse", "HEAD"], path = path)
        code = result["code"]
        if not code == 0: return None
        message = result.get("stdout", "")
        commit = message.strip()
        return commit

    @classmethod
    def get_branches(cls, path = None):
        path = path or common.base().get_base_path()
        result = util.execute(["git", "branch"], path = path)
        code = result["code"]
        if not code == 0: return None
        message = result.get("stdout", "")
        branches = message.strip()
        branches = branches.split("\n")
        branches = [(value.lstrip("* "), value.startswith("*")) for value in branches]
        return branches

    @classmethod
    def get_branch(cls, path = None):
        path = path or common.base().get_base_path()
        branches = cls.get_branches(path = path)
        for branch, selected in branches:
            if not selected: continue
            return branch
        return None
