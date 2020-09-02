# coding: utf-8

"""
    KS- Trade API



    The version of the OpenAPI document: 1.0

"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "openapi-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="KS- Trade API",
    author="KS API team",
    author_email="team@ksapi.com",
    url="",
    keywords=["OpenAPI", "KS- Trade API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\

    """
)
