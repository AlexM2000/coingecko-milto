import os

from pip._internal.req import parse_requirements
from setuptools import find_packages, setup

install_reqs = parse_requirements("requirements.txt", session="hack")
version = str(os.environ.get('BUILD_BUILDNUMBER', 1))

setup(
  name="coingecko_milto",
  version=version,
  packages=find_packages(exclude=["tests", "tests*"]),
  include_package_data=True,
  install_requires=[str(ir.requirement) for ir in install_reqs],
  test_suite="tests",
  entry_points={
      'console_scripts': [
          'etl = milto:run'
      ]
  }
)
