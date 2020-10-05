import os
from abc import abstractmethod

defaultValues = {
    "SQL_USER": "postgres",
    "SQL_PASSWORD": "postgres",
    "SQL_DB": "i2b2_data",
    "SQL_HOST": "db",
    "SQL_PORT": 5432,
    "FLASK_PORT":"8080"
}


class AbstractConfig(object):
    """
    Parent Class containing get_property to return the ENV variable of default value if not
    found.
    """
    def __init__(self):
        self._defaultValues = defaultValues

    def get_property(self, property_name):
        if os.getenv(property_name) is not None:
            return os.getenv( property_name)
        if property_name not in self._defaultValues.keys():  # we don't want KeyError
            return None  # No default value found
        # return default value
        return self._defaultValues[property_name]



class Config(AbstractConfig):
    """
    THis Class is ued to provide hard coded values to the application, first using environment variables
    and if not found,  defaulting to those values provided in the defaultValues dictionary above.

    """

    @property
    def flask_port(self):
        return self.get_property('FLASK_PORT')

    @property
    def sql_user(self):
        return self.get_property('SQL_USER')

    @property
    def sql_password(self):
        return self.get_property('SQL_PASSWORD')

    @property
    def sql_db(self):
        return self.get_property('SQL_DB')

    @property
    def sql_port(self):
        return self.get_property('SQL_PORT')

    @property
    def sql_host(self):
        return self.get_property('SQL_HOST')