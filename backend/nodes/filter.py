from backend.nodes.base import BaseNode
from backend.nodes.registry import register_node

@register_node
class BandpassFilterNode(BaseNode):
    @classmethod
    def category(cls):
        return "Filters"

    def run(self, data=None):
        l_freq = self.config.get("l_freq", 1.0)
        h_freq = self.config.get("h_freq", 40.0)
        if data is None:
            raise ValueError("No input data provided.")
        return data.filter(l_freq=l_freq, h_freq=h_freq)
