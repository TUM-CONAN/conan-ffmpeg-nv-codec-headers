#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class FFMpegNVCodecHeadersConan(ConanFile):
    name = "ffmpeg-nv-codec-headers"
    version = "9.0.18.1"
    url = "https://github.com/ulricheck/conan-ffmpeg-nv-coded-headers"
    description = "FFmpeg NV Codec Headers"
    license = "https://github.com/someauthor/somelib/blob/master/LICENSES"
    exports_sources = ["LICENSE"]
    no_copy_source = True

    def source(self):
        extracted_dir = "nv-codec-headers-n%s" % self.version
        archive_name = "nv-codec-headers-%s.tar.gz" % self.version
        source_url = "https://github.com/FFmpeg/nv-codec-headers/releases/download/n%s/%s" % (self.version, archive_name)
        tools.get(source_url)
        os.rename(extracted_dir, "sources")
        os.rename(os.path.join("sources", "ffnvcodec.pc.in"), os.path.join("sources", "ffnvcodec.pc"))


    def build(self):
        pass

    def package(self):
        self.copy(pattern='*.h', src='sources/include', dst='include', keep_path=True)
        self.copy(pattern='ffnvcodec.pc', src='sources', dst="lib/pkgconfig", keep_path=False)

    def package_id(self):
        self.info.header_only()
