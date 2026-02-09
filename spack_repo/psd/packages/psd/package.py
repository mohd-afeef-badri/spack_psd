# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Psd(AutotoolsPackage):
    """
    PSD (Parallel finite element Solver for continuum Dynamics) is a 
    high-performance  finite  element  solver  for  solid  mechanics
    applications. Designed for largescale simulations, it is capable
    of solving problems with large numberof unknowns in both  static
    & dynamic  regimes, with support for linear and nonlinear models 
    """
    homepage = "https://mohd-afeef-badri.github.io/psd"
    url = "https://github.com/mohd-afeef-badri/psd/archive/0a67ccbdf2585cb8250ac3c935ae9a27b533f822.tar.gz"
    git = "https://github.com/mohd-afeef-badri/psd.git"

    maintainers("mohd-afeef-badri")

    license("Apache-2.0", checked_by="mohd-afeef-badri")

#    version("main", commit="56267508db3b209a487c0d217116ca5b841f91ce")
    version("main", branch="main")

    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")

    depends_on("tfel")
    depends_on("mgis")
    depends_on("freefem+mpi+petsc")
    depends_on("petsc+mpi+hpddm+mumps")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")
