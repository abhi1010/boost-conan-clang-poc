from conans import ConanFile, CMake

class ExampleConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = ("boost/1.72.0",)
    generators = "txt"


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test() # Build the "RUN_TESTS" or "test" target
        cmake.install()
