from distutils.core import setup, Extension
factorial_module = Extension('cmath1', sources=['cmath.c'])
setup(name='MathExtension', version='1.0', description='This is a math package', ext_modules=[factorial_module])
