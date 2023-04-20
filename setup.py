from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gms/__init__.py
from gms import __version__ as version

setup(
	name="gms",
	version=version,
	description="Gym Management Systeam",
	author="Aadith",
	author_email="aadith.p@sigzen@123#",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
