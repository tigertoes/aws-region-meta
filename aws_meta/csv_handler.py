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

import csv
import unicodecsv
import distutils
import json


class CSVHandler():
    """ CSV Handler processes the main spreadsheet of information in data/.

    Here is probably a good reason to briefly explain why I went with storing stuff
    as a spreadsheet in the first place - the short answer is, it's just simply
    easier to manage. At the moment given the tables across Amazon's documentation
    are a little too inconsistent for automated parsing, so most of the data is
    manually put in by the author.
    """

    def __init__(self, csv_file):
        """
        :param csv_file: Filehandle of the CSV file to parse, must be UTF-8 w/BOM 
        """
        # utf-8-sig signifies there's a Unicode BOM
        self.reader = unicodecsv.DictReader(csv_file, encoding='utf-8-sig')
        self.data = {}

    def to_json(self):
        """ Serialise the data out as JSON """
        return json.dumps(self.data)

    def restructure(self):
        """ Turn a CSV into a structured data form

        Column values are expected to be ```[\d\w_\.]```, with whitespace being
        stripped out. anything with a "." will get split out into it's own dict.
        A column called 'name' must be present as the region identifier.
        """
        self.data = {}
        for row in self.reader:
            region = {}
            region_name = ''
            for col in self.reader.fieldnames:
                if row[col] == '':
                    continue
                c_col = col.replace(' ', '')
                if c_col == 'name':
                    region_name = row[col]
                elif "." in c_col:
                    (service, feature) = c_col.split('.')
                    if not service in region:
                        region[service] = {}
                    region[service][feature] = row[col]
                elif c_col == 'restricted':
                    region[u'restricted'] = bool(distutils.util.strtobool(row[col]))
                elif c_col == 'az_count':
                    region['availability_zones'] = self.generate_az(region_name, int(row[col]))
                elif c_col != '':
                    region[c_col] = row[col]

            self.data[region_name] = region

    def generate_az(self, region, total_az):
        """ 
        Amazon Availability Zones are just auto-incrementing letters on top of
        the region name.
        :param region: Name of the region, e.g "eu-west-1"
        :param total_az: Number of availability zones
        :return: list containing all the AZs
        """
        return list(map(lambda x: region + chr(ord('a') + x), range(total_az)))
