"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, info):
        """Instantiate a new `NearEarthObject`.

        Args:
        info {dict} -- Excess keyword arguments specifying all required info about the NEO.
        """
        self.designation = info['pdes']
        self.name = info['name'] if not info['name'] == '' else None
        self.diameter = float(
            info['diameter']) if info['diameter'] else float('nan')
        self._pha = info['pha']
        self._full_name = info['full_name']

        self.approaches = set()

    @property
    def hazardous(self):
        """Bool to confirm if this NEO is classed as hazardous or not. Note a lack of hazard status == not hazardous."""
        mapping = {'Y': True, 'N': False}
        return mapping.get(self._pha) if self._pha else False

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self._full_name:
            return self._full_name.strip()
        else:
            if not self.name:
                self.name = ''
            return f"{self.designation} {self.name}".strip()

    def __str__(self):
        """Return `str(self)`."""
        return f"{self.fullname} has a diameter of {self.diameter:.3f} and a hazard status of {self.hazardous}."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initialized as None, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, info):
        """
        Instantiate a new `CloseApproach`.

        Args:
        info {dict} -- Excess keyword arguments specifying all required info about the Close Approach.
        """
        self._designation = info['des']
        self.time = cd_to_datetime(info['cd'])
        self.distance = float(info['dist'])
        self.velocity = float(info['v_rel'])
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        if hasattr(self.neo, '_full_name'):
            name = self.neo._full_name
        else:
            name = self._designation
        return (f"{name} was/will be {self.distance: .2f} au away from Earth on "
                f"{self.time_str} travelling at {self.velocity: .2f}km/s.")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
