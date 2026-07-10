from setuptools import setup, find_packages

setup(
    name="quant-real-estate-engine",
    version="0.1.0",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        # Add any dependencies required by the core mathematical package here
    ],
)