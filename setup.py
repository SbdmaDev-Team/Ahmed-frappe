from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ahmed/__init__.py
from ahmed import __version__ as version

setup(
	name="ahmed",
	version=version,
	description="test",
	author="ahmed hori",
	author_email="ahmedaldobhany446@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
