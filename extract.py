"""Transform NASAs large files containing NEO data into python-friendly collections."""

import csv
import json
from models import NearEarthObject, CloseApproach
from collections import OrderedDict


def load_neos(neo_csv_path):
    """Produce a collection of near-Earth objects after reading the information from a CSV file.

    neo_csv_path {Path-like object} -- A path to a CSV file containing data about near-Earth objects.
    """
    with open(neo_csv_path) as f:
        nc = csv.DictReader(f)
        neos = [NearEarthObject(row) for row in nc]
    return neos


def load_approaches(cad_json_path):
    """Produce a collection of CloseApproach objects after reading the information from a json file.

    cad_json_path {Path-like object} -- A path to a CSV file containing data about near-Earth objects.
    """
    neos = []
    with open(cad_json_path) as f:
        cad_json = json.load(f)
        neos = [CloseApproach(row) for row in [OrderedDict(zip(cad_json['fields'], row))
                                               for row in cad_json['data']]]
    return neos
