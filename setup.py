from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'TNG statement parser python package'
LONG_DESCRIPTION = 'tngparser is a python library to helps to parse Touch n Go eWallet and card statements'

required = []
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
        name="tngparser", 
        version=VERSION,
        author="Hao Quan Tang",
        author_email="tanghq33@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=required,        
        keywords=['python', 'tng', 'financial', 'parser', 'ewallet'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)