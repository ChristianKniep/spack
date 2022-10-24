# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Bbmap(Package, SourceforgePackage):
    """Short read aligner for DNA and RNA-seq data."""

    homepage = "https://sourceforge.net/projects/bbmap/"
    sourceforge_mirror_path = "bbmap/BBMap_38.63.tar.gz"

    version("38.93", sha256="e2700cc6bfa6ff0868bb2887850f1e514bc6e44cd71ca933e23ae5ce3c630605")
    version("38.63", sha256="089064104526c8d696164aefa067f935b888bc71ef95527c72a98c17ee90a01f")
    version("37.36", sha256="befe76d7d6f3d0f0cd79b8a01004a2283bdc0b5ab21b0743e9dbde7c7d79e8a9")

    depends_on("java")

    def install(self, spec, prefix):
        install_tree(".", prefix.bin)

    def setup_run_environment(self, env):
        env.set("BBMAP_CONFIG", self.prefix.bin.config)
        env.set("BBMAP_RESOURCES", self.prefix.bin.resources)
