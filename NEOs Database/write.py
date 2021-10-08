"""Module used to write CloseApproach objects to user's choice of csv or json file in a specified or default location."""

import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename=None):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    Args:
    results {iterable of CloseApproach objects} -- the data that will be written to file
    filename {Path-like object} -- the location at which the file will be written (defaults to ./results.csv)
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s',
                  'designation', 'name', 'diameter_km', 'potentially_hazardous')

    filename = filename if filename else 'results.csv'
    output = [fieldnames]
    for approach in results:
        neo = approach.neo
        output.append((datetime_to_str(approach.time), approach.distance, approach.velocity, neo.designation,
                      neo.name if neo.name else '', neo.diameter if neo.diameter else 'nan', neo.hazardous))
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for elem in output:
            writer.writerow(elem)


def write_to_json(results, filename=None):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    Args:
    results {iterable of CloseApproach objects} -- the data that will be written to file
    filename {Path-like object} -- the location at which the file will be written (defaults to ./results.json)
    """
    filename = filename if filename else 'results.json'
    output = []
    for approach in results:
        neo = approach.neo
        output.append({"datetime_utc": datetime_to_str(approach.time), "distance_au": float(approach.distance),
                       "velocity_km_s": float(approach.velocity), "neo": {"designation": str(neo.designation), "name": neo.name if neo.name else '',
                                                                          "diameter_km": float(neo.diameter if neo.diameter else 'nan'), "potentially_hazardous": neo.hazardous}})
    with open(filename, 'w') as f:
        json.dump(output, f)
