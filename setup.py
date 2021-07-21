# Copyright 2020 Pasqal Cloud Services development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup

__version__ = ""
exec(open("sdk/_version.py").read())

setup(
    name="sdk",
    version="0.0.1",
    description="Software development kit for Pasqal cloud platform.",
    packages=find_packages(),
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    maintainer="Pasqal Cloud Services",
    maintainer_email="pcs@pasqal.io",
    python_requires=">=3.7.0",
    license="Apache 2.0",
    # TODO:
    classifiers=[],
    url="https://github.com/pasqal-io/cloud-sdk",
    install_requires=[
        "requests==2.25.1",
    ],
    extras_require={
        "dev": {
            "black==20.8b1",
            "flake8==3.9.0",
            "flake8-import-order==0.18.1",
        }
    },
)