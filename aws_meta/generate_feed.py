# Copyright 2017 aws-meta authors.
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

import os
from time import strftime

from argparse import ArgumentParser
from csv_handler import CSVHandler


def main():
    parser = ArgumentParser()
    parser.add_argument('--csv_file', '-c', dest='csv_file', required=True, metavar='FILE',
                        help='CSV containing region metadata',
                        type=lambda x: valid_file(parser, x))
    parser.add_argument('--api_version', '-a', dest='api_version', required=True,
                        default=strftime('%Y-%m-%d'),
                        help='Version of API')
    parser.add_argument('--basedir', '-b', dest='base_dir', required=True,
                        help='Base directory to write feeds out to')
    args = parser.parse_args()
    csv = CSVHandler(args.csv_file)
    csv.restructure()

    version_directory = os.path.join([args.base_dir, args.api_version])
    latest_directory = os.path.join([args.base_dir, 'latest'])

    for directory in (version_directory, latest_directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            with open(os.path.join([directory, 'regions.json']), 'w') as f:
                f.write(csv.to_json())


def valid_file(parser, filepath):
    """Open the file if it's valid, else throw a parser error"""
    if os.path.isfile(filepath):
        return open(filepath, 'r')
    else:
        parser.error("%s doesn't appear to be a valid file!" % file)


if __name__ == '__main__':
    main()
