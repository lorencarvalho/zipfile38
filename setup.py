from distutils.core import setup

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name='zipfile38',
    version='0.0.3',
    description='Read and write ZIP files - backport of the zipfile module from Python 3.8',
    long_description = readme,
    author='Loren Carvalho',
    url='https://github.com/lorencarvalho/zipfile38',
    py_modules=['zipfile38'],
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Archiving :: Compression',
    ],
)
