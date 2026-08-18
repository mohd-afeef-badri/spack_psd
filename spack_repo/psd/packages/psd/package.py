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
    url = "https://github.com/mohd-afeef-badri/psd/archive/refs/tags/v2.6.tar.gz"
    git = "https://github.com/mohd-afeef-badri/psd.git"

    maintainers("mohd-afeef-badri")

    license("Apache-2.0", checked_by="mohd-afeef-badri")

    version("main", branch="main")
    version("2.6", sha256="5716e91e7fc79ffd125976fba0db9373b2e01a00883fb17e6b033d077fbf1888")
    version("2.5", sha256="16ec15f5baf78e1d9466db78ae4f34a160d585bc11665c835c829809ecc6e657")
    version("2.4", sha256="ba7916bc844ab635fda2b6fdae956d2f27baeb44669f3c2a5280b81dec5339b6")
    version("2.3", sha256="b82fd1beb99c65b5a64f60370cdff78b9b2c7466366168e1d6da6c3db025a3af")
    version("2.2", sha256="f3b1b258976ea69be825ed64004acda7d3a865da003ecd4c7dfa1e38f6a5391c")
    version("2.1", sha256="24e905361c821b7789f77c6ec8012cb2ae36903e421f1a76efba3f05ca32c777")
    version("2.0", sha256="d59fce3add565f3b9b0e56723c31ed06016704ca6f0af108f30e6ef1d2fde10c")

    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("gmsh~fltk~med", type=("build", "run"))

    depends_on("tfel")
    depends_on("mgis")
    depends_on("freefem+mpi+petsc~superlu")
    depends_on("petsc+mpi+hpddm+mumps+metis")

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")
