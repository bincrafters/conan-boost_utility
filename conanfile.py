#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostUtilityConan(base.BoostBaseConan):
    name = "boost_utility"
    url = "https://github.com/bincrafters/conan-boost_utility"
    lib_short_names = ["utility"]
    header_only_libs = ["utility"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits"
    ]
