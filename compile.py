from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("q_learning",  ["q_learning.py"]),
    # ... all your modules that need be compiled ...]setup(
    Extension("ql_runner",  ["ql_runner.py"]),

]

setup(
    name='ql-learn',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
