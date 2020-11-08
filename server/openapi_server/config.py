import os
# from abc import abstractmethod

defaultValues = {
    "SERVER_PROTOCOL": "http://",
    "SERVER_HOST": "localhost",
    "SERVER_PORT": "8080"
}


class AbstractConfig(object):
    """
    Parent Class containing get_property to return the ENV variable of default
    value if not found.
    """
    def __init__(self):
        self._defaultValues = defaultValues

    def get_property(self, property_name):
        if os.getenv(property_name) is not None:
            return os.getenv(property_name)
        # we don't want KeyError?
        if property_name not in self._defaultValues.keys():
            return None  # No default value found
        # return default value
        return self._defaultValues[property_name]


class Config(AbstractConfig):
    """
    THis Class is ued to provide hard coded values to the application, first
    using environment variables and if not found,  defaulting to those values
    provided in the defaultValues dictionary above.
    """

    @property
    def server_protocol(self):
        return self.get_property('SERVER_PROTOCOL')

    @property
    def server_host(self):
        return self.get_property('SERVER_HOST')

    @property
    def server_port(self):
        return self.get_property('SERVER_PORT')

    @property
    def server_url(self):
        return "%s%s:%s" % (self.server_protocol, self.server_host,
                            self.server_port)

    @property
    def server_api_url(self):
        return "%s%s:%s%s" % (self.server_protocol, self.server_host,
                              self.server_port, "/api/v1")

    # @property
    # def sql_user(self):
    #     return self.get_property('SQL_USER')

    # @property
    # def sql_password(self):
    #     return self.get_property('SQL_PASSWORD')

    # @property
    # def sql_db(self):
    #     return self.get_property('SQL_DB')

    # @property
    # def sql_port(self):
    #     return self.get_property('SQL_PORT')

    # @property
    # def sql_host(self):
    #     return self.get_property('SQL_HOST')
