from elasticsearch7 import Elasticsearch, helpers

from configs import LOGGER
from models.base import ESConnectionMeta


class ESConnector:

    _meta: ESConnectionMeta
    _client: Elasticsearch

    def __init__(self, meta: ESConnectionMeta) -> None:
        self._meta = meta

    def __enter__(self) -> "ESConnector":
        """
        Connect to the Elasticsearch server and return the connection object.

        :return: The connection object.
        :rtype: ESConnector
        :raises ValueError: If the connection to the Elasticsearch server fails.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection to the Elasticsearch server.

        This method is called when the context manager exits its scope.
        """
        self.close()

    def connect(self) -> None:
        """
        Connect to the Elasticsearch server and return the connection object.

        :return: The connection object.
        :rtype: ESConnector
        :raises ValueError: If the connection to the Elasticsearch server fails.
        """
        try:
            self._client = Elasticsearch(self._meta.uri_string(base="http"))
            LOGGER.info("Elasticsearch connected.")
        except Exception as e:
            raise e

    def close(self) -> None:
        """
        Close the connection to the Elasticsearch server.
        """
        if hasattr(self, "_client") and self._client:
            self._client.close()
        LOGGER.info("Elasticsearch disconnected.")
