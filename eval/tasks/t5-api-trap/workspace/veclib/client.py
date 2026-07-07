class Client:
    """Vector search client.

    Parameters:
        host: server host name
        port: server port (default 6333)
        timeout_s: request timeout in seconds (default 30)
        retries: number of retries on transient errors (default 3)
    """

    def __init__(self, host, port=6333, timeout_s=30, retries=3):
        self.host = host
        self.port = port
        self.timeout_s = timeout_s
        self.retries = retries

    def search(self, vector, top_k=10, filter=None):
        """Return the top_k nearest neighbours of vector."""
        raise NotImplementedError("network client stub")
