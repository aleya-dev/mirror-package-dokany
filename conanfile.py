from conan import ConanFile
from conan.tools.files import copy
import os


required_conan_version = ">=2.0"


class DokanyConan(ConanFile):
    name = "dokany"
    version = "2.1.0.1000"
    settings = "os", "arch", "compiler", "build_type"

    def layout(self):
        self.folders.build = "C:/Program Files/Dokan/Dokan Library-2.1.0/"
        self.folders.source = self.folders.build

    def package(self):
        copy(self, "*.lib",
            os.path.join(self.build_folder, 'lib'),
            os.path.join(self.package_folder, "lib"),
            keep_path=False)

        copy(self, "*.dll",
            self.build_folder,
            os.path.join(self.package_folder, "bin"),
            keep_path=False)

        copy(self, "*",
            os.path.join(self.build_folder, 'include'),
            os.path.join(self.package_folder, "include"),
            keep_path=True)

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "dokany")

        self.cpp_info.components['dokan2'].libs = ['dokan2']
        self.cpp_info.components['dokan2'].set_property("cmake_target_name", "dokany::dokany")

        self.cpp_info.components['dokan2fuse'].libs = ['dokanfuse2']
        self.cpp_info.components['dokan2fuse'].set_property("cmake_target_name", "dokany::fuse")
        self.cpp_info.components['dokan2fuse'].requires = ['dokan2']

        self.cpp_info.components['dokan2np'].libs = ['dokannp2']
        self.cpp_info.components['dokan2np'].set_property("cmake_target_name", "dokany::np")
        self.cpp_info.components['dokan2np'].requires = ['dokan2']
