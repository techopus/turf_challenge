from datetime import datetime


class Pitch:
    def __init__(self, name, location, turf_type, last_maintenance_date, next_scheduled_maintenance, current_condition, replacement_date):
        self.name = name
        self.location = location
        self.turf_type = turf_type
        self.last_maintenance_date = last_maintenance_date
        self.next_scheduled_maintenance = next_scheduled_maintenance
        self.current_condition = current_condition
        self.replacement_date = replacement_date

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'turf_type': self.turf_type,
            'last_maintenance_date': self.last_maintenance_date,
            'next_scheduled_maintenance': self.next_scheduled_maintenance,
            'current_condition': self.current_condition,
            'replacement_date': self.replacement_date
        }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise ValueError("Location must be a string")
        self._location = value

    @property
    def turf_type(self):
        return self._turf_type

    @turf_type.setter
    def turf_type(self, value):
        if value not in ['Natural', 'Artificial', 'Hybrid']:
            raise ValueError("Turf type must be one of 'Natural', 'Artificial', or 'Hybrid'")
        self._turf_type = value

    @property
    def last_maintenance_date(self):
        return self._last_maintenance_date

    @last_maintenance_date.setter
    def last_maintenance_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Last maintenance date must be a datetime object")
        self._last_maintenance_date = value

    @property
    def next_scheduled_maintenance(self):
        return self._next_scheduled_maintenance

    @next_scheduled_maintenance.setter
    def next_scheduled_maintenance(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Next scheduled maintenance must be a datetime object")
        self._next_scheduled_maintenance = value

    @property
    def current_condition(self):
        return self._current_condition

    @current_condition.setter
    def current_condition(self, value):
        if not isinstance(value, int) or value < 0 or value > 10:
            raise ValueError("Current condition must be an integer between 0 and 10")
        self._current_condition = value

    @property
    def replacement_date(self):
        return self._replacement_date

    @replacement_date.setter
    def replacement_date(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Replacement date must be a datetime object")
        self._replacement_date = value
