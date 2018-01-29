# Copyright 2018 aws-meta authors.
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

from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
    name='aws-meta',
    version=VERSION,
    author='Tony Tiger',
    author_email='thatrascaltiger@gmail.com',
    license='Apache 2',
    install_requires=['unicodecsv'],
    setup_requires=['flake8', 'sphinx', 'genson'],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['aws_feed = aws_meta.generate_feed:main']
    },
    test_suite='test'
)
