from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

print("Numpy include output is",numpy.get_include())

extensions = [
    Extension("cython_test", ["cython_test.pyx"],
              include_dirs = [numpy.get_include()],
              )
]

setup(
    name = "cython_test",
    ext_modules = cythonize(extensions)
    )
