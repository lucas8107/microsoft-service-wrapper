#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["msal~=1.17.0", "requests~=2.27.1"]

test_requirements = ["pytest==7.1.1"]

setup(
    author="Lucas Paula",
    author_email="luolcami@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="A python wrapper for microsoft services REST API (currently: Graph and PowerBI)",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="microsoft_service_wrapper",
    name="microsoft_service_wrapper",
    packages=find_packages(
        include=["microsoft_service_wrapper", "microsoft_service_wrapper.*"]
    ),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/lucas8107/microsoft-service-wrapper",
    version='0.4.0',
    zip_safe=False,
)
