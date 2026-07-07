class Client:
    """Vector search client."""

    def __init__(self, host, port=6333, timeout_s=30):
        self.host = host
        self.port = port
        self.timeout_s = timeout_s

    def search(self, vector, top_k=10, filter=None):
        """Return the top_k nearest neighbours of vector."""
        raise NotImplementedError("network client stub")

    def delete(self, ids, wait=True):
        """Delete points by id. If wait, block until applied."""
        raise NotImplementedError("network client stub")
