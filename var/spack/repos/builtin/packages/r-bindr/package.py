# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RBindr(RPackage):
    """Provides a simple interface for creating active bindings where the
       bound function accepts additional arguments."""

    homepage = "https://github.com/krlmlr/bindr"
    url      = "https://cran.r-project.org/src/contrib/bindr_0.1.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/bindr"

    version('0.1', 'f3897a70cbad2d2981272772fa30bb59')
