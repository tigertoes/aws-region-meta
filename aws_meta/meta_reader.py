import json
import os


class MetaReader:
    """ Provide a rudimentary API to query the data set

    Worth noting that this works only against the latest set, so the structure
    does not come with any real sort of guarantees.
    """
    def __init__(self):
        filepath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../', 'api', 'latest'
        ) + '/regions.json'
        with open(filepath) as f:
            self.payload = json.load(f)

    def get_region(self, region):
        """ Return a dictionary containing regional information"""
        return self.payload.get(region)
