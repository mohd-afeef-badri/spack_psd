# Copyright Spack Project Developers. See COPYRIGHT file for details. 
# 
# SPDX-License-Identifier: (Apache-2.0 OR MIT) 
 
from spack_repo.builtin.build_systems.autotools import AutotoolsPackage 
 
from spack.package import * 
 
 
class Freefempsd(AutotoolsPackage): 
    """FreeFEM is a popular 2D and 3D partial differential equations (PDE) solver. 
    It allows you to easily implement your own physics modules using the provided 
    FreeFEM language. FreeFEM offers a large list of finite elements, like the 
    Lagrange, Taylor-Hood, etc., usable in the continuous and discontinuous 
    Galerkin method framework. 
    """ 
 
    homepage = "https://freefem.org" 
    url = "https://github.com/FreeFem/FreeFem-sources/archive/refs/tags/v4.15.tar.gz" 
    git = "https://github.com/FreeFem/FreeFem-sources.git" 
 
    maintainers("corentin-dev") 
 
    license("LGPL-3.0-only", checked_by="mohd-afeef-badri") 
 
    version("develop", branch="develop") 
    version("4.15", sha256="a47af5a7c7006ae8c648845e55d732ea403837af869493000a008b2013c698e3") 
    version("4.14", sha256="931cbfe9ef6f6530756c300c5ae47bfdaca21c560a5407cb33325a376a3b6af8") 
    version("4.13", sha256="aefd4ff02333209f7433abef2e74acb621b6946063ff27e81cf2da43120b6ae4") 
    version("4.12", sha256="291c5f46761711d6303914f9c4f165fd85a7b7b69141f7473e0b6484ce6ab0f5") 
    version("4.11", sha256="d0c6921791e5f94646d8dde4d9ed3c11b979e47e7bbb3c0a66467b04dd56983a") 
    version("4.10", sha256="957994c8f24cc2a671b8c116ae530796c3a431d4157ee71a3d6aab7122e7570d") 
 
    variant("mpi", default=False, description="Activate MPI support") 
    variant("petsc", default=False, description="Compile with PETSc/SLEPc") 
    variant("superlu", default=True, description="Activate SuperLU support") 
 
    depends_on("c", type="build")  # generated 
    depends_on("cxx", type="build")  # generated 
    depends_on("fortran", type="build")  # generated 
 
    depends_on("autoconf", type="build") 
    depends_on("automake", type="build") 
    depends_on("libtool", type="build") 
 
    depends_on("bison", type="build") 
    depends_on("flex", type="build") 
    depends_on("m4", type="build") 
    # depends_on("patch", type="build") 
    # depends_on("unzip", type="build") 
 
    depends_on("lapack") 
 
    depends_on("mpi", when="+mpi") 
    depends_on("slepc", when="+petsc")
 
    def configure_args(self): 
        spec = self.spec 
        options = [ 
            "--disable-mkl", 
            "CFLAGS=%s" % " ".join(spec.compiler_flags["cflags"]), 
            "FFLAGS=%s" % " ".join(spec.compiler_flags["fflags"]), 
            "CXXFLAGS=%s" % " ".join(spec.compiler_flags["cxxflags"]), 
        ] 
 
        if spec.satisfies("+petsc"): 
            options.append("--with-petsc=%s" % spec["petsc"].prefix.lib.petsc.conf.petscvariables) 
            options.append("--with-slepc-ldflags=%s" % spec["slepc"].libs.ld_flags) 
            options.append("--with-slepc-include=%s" % spec["slepc"].headers.include_flags) 
        else: 
            options.append("--without-petsc") 
            options.append("--without-slepc") 
 
        if spec.satisfies("~superlu"): 
            options.append("--disable-superlu") 
 
        return options 

