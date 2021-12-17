# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class ExtendsSpec(Package):
    """Package that tests if the extends directive supports a spec."""

    homepage = "http://www.example.com"
    url = "http://www.example.com/example-1.0.tar.gz"

    version('1.0', '0123456789abcdef0123456789abcdef')

    extends('extendee@1:')