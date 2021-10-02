"""To facilitate more advanced querying of CloseApproaches; specifying a number of optional filters."""

from helpers import cd_to_datetime
from itertools import islice


def create_filters(date=None, start_date=None, end_date=None,
                   distance_min=None, distance_max=None,
                   velocity_min=None, velocity_max=None,
                   diameter_min=None, diameter_max=None,
                   hazardous=None):
    """Create a dictionary of filters from user-specified criteria.

    The return value must be compatible with the `query` method of `NEODatabase`.

    Args:
    date {datetime.date} -- A date on which a matching `CloseApproach` occurs.
    start_date {datetime.date} -- A date on or after which a matching `CloseApproach` occurs.
    end_date {datetime.date} -- A date on or before which a matching `CloseApproach` occurs.
    distance_min {numeric} -- A minimum nominal approach distance for a matching `CloseApproach`.
    distance_max {numeric} -- A maximum nominal approach distance for a matching `CloseApproach`.
    velocity_min {numeric} -- A minimum relative approach velocity for a matching `CloseApproach`.
    velocity_max {numeric} -- A maximum relative approach velocity for a matching `CloseApproach`.
    diameter_min {numeric} -- A minimum diameter of the NEO of a matching `CloseApproach`.
    diameter_max {numeric} -- A maximum diameter of the NEO of a matching `CloseApproach`.
    hazardous {Boolean} - Whether the NEO of a matching `CloseApproach` is potentially hazardous.
    """
    kwargs = {}
    if date:
        kwargs.update({'date': date})
    if start_date:
        kwargs.update({'start_date': start_date})
    if end_date:
        kwargs.update({'end_date': end_date})
    if distance_min:
        kwargs.update({'distance_min': distance_min})
    if distance_max:
        kwargs.update({'distance_max': distance_max})
    if velocity_max:
        kwargs.update({'velocity_max': velocity_max})
    if velocity_min:
        kwargs.update({'velocity_min': velocity_min})
    if diameter_min:
        kwargs.update({'diameter_min': diameter_min})
    if diameter_max:
        kwargs.update({'diameter_max': diameter_max})
    if not hazardous is None:
        kwargs.update({'hazardous': hazardous})

    return kwargs


def limit(iterator, n=None):
    """Produce (at most) the first n values of the input iterator.

    If `n` is 0 or None, don't limit the iterator at all.

    iterator {iterable} -- An iterator of values.
    n {int} -- The maximum number of values to produce.
    """
    return islice(iterator, n) if n else iterator
