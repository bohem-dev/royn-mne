class BaseNode:
    def __init__(self, config=None):
        self.config = config or {}

    @classmethod
    def name(cls):
        return cls.__name__

    @classmethod
    def category(cls):
        return "Uncategorized"

    def run(self, data=None):
        raise NotImplementedError("Each node must implement the run method.")

    def to_dict(self):
        return {
            "type": self.name(),
            "category": self.category(),
            "config": self.config
        }

    @classmethod
    def from_dict(cls, data):
        return cls(config=data.get("config", {}))
