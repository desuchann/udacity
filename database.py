"""For instantiation of a database containing all the NEO and associated CloseApproach data to facilitate user-defined querying."""

import operator


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """

    def __init__(self, neos, approaches):
        """Instantiate a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        Args:
        neos {NearEarthObjects} -- A collection of `NearEarthObject`s.
        approaches {CloseApproaches} -- A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        self.pdes_to_neo = {neo.designation: neo for neo in self._neos}
        self.name_to_pdes = {
            neo.name: neo.designation for neo in self._neos if neo.name}
        self.approach_to_des = {
            approach: approach._designation for approach in self._approaches}

        for approach in self._approaches:
            neo = self.get_neo_by_designation(approach._designation)
            approach.neo = neo
            neo.approaches.add(approach)

    def __str__(self):
        """Return `str(self)`."""
        return f"NEODatabase linking {len(self._neos)} near-Earth objects to {len(self._approaches)} close-Earth approaches."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"A database linking near-Earth objects to their respective close-Earth approaches."

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        - If no match is found, return `None` instead.
        - Each NEO in the data set has a unique primary designation, as a string.
        - The matching is exact - check for spelling and capitalization if no
        match is found.

        Args:
        designation {int} -- The primary designation of the NEO to search for.
        """
        return self.pdes_to_neo.get(designation)

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        - If no match is found, return `None` instead.
        - Not every NEO in the data set has a name.
        - The matching is exact - check for spelling and capitalization if no
        match is found.

        Args:
        name {str} -- The name, as a string, of the NEO to search for.
        """
        return self.pdes_to_neo.get(self.name_to_pdes.get(name))

    def query(self, args):
        """Query close approaches to generate those that match a collection of filters.

        - This generates a stream of `CloseApproach` objects that match all of the
        provided filters.
        - If no arguments are provided, generate all known close approaches.
        - The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaningfully, although is often sorted by time.

        Args:
        filters {dict} --- A collection of filters capturing user-specified criteria.
        """

        def _check_args(approach, args):
            """To facilitate querying by returning a Bool after comparing each CloseApproach to the user-defined filters."""
            eq = operator.eq
            le = operator.le
            ge = operator.ge

            mapping = {'des': (approach._designation, eq), 'date': (approach.time.date(), eq), 'start_date': (approach.time.date(), ge),
                       'end_date': (approach.time.date(), le), 'distance_min': (float(approach.distance), ge), 'distance_max': (float(approach.distance), le),
                       'velocity_max': (float(approach.velocity), le), 'velocity_min': (float(approach.velocity), ge), 'name': (approach.neo.name, eq),
                       'diameter_min': (float(approach.neo.diameter), ge), 'diameter_max': (float(approach.neo.diameter), le), 'hazardous': (approach.neo.hazardous, eq)}

            for key in args.keys():
                op = mapping.get(key)
                if not op:
                    raise KeyError('No option to search for %s' % key)

                # no key = continue the query
                # key that matches = continue the query
                # key that doesn't match = start the query over
                if args.get(key) is None:
                    yield True
                else:
                    yield op[1](op[0], args.get(key))

        if not args:  # return everything by default
            for approach in self._approaches:
                yield approach

        else:
            for approach in self._approaches:
                if not all(_check_args(approach, args)):
                    continue
                else:
                    yield approach
