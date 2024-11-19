from connections.elasticsearch import ESConnector, ESConnectionMeta, helpers


class MainHandler:
    def __init__(self, elastic: ESConnector):
        self.elastic = elastic


if __name__ == "__main__":
    meta = ESConnectionMeta(
        host="localhost", port=9200, username="elastic", password="password"
    )
    with ESConnector(meta) as elastic:
        handler = MainHandler(elastic)
