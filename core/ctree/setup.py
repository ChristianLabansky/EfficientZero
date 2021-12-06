from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np

# setup(ext_modules=cythonize('cytree.pyx'), extra_compile_args=['-O3'], include_dirs=[np.get_include()])

extensions = [
    Extension("cytree", ["cytree.pyx"],
        include_dirs=[np.get_include()]
    )
    # Everything but primes.pyx is included here.
    # Extension("*", ["*.pyx"],
    #     include_dirs=[...],
    #     libraries=[...],
    #     library_dirs=[...]),
]

setup(
    name="efficientzero",
    ext_modules=cythonize(extensions),
)