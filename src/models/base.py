from typica import URIConnectionMeta, AuthMeta, EndpointMeta


class ESConnectionMeta(URIConnectionMeta, AuthMeta, EndpointMeta):
    ...

    def uri_string(self, base: str = "http") -> str:
        """
        Return a URI string for the database connection.

        :param base: The base of the URI (e.g. "http", "https", etc.).
        :return: A string representing the URI.
        """
        meta = f"{self.host}:{self.port}"
        if self.username:
            return f"{base}://{self.username}:{self.password}@{meta}"
        return f"{base}://{meta}"
