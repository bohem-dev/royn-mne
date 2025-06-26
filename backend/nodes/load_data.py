from mne.io import read_raw_fif
from backend.nodes.base import BaseNode
from backend.nodes.registry import register_node

@register_node
class LoadDataNode(BaseNode):
    @classmethod
    def category(cls):
        return "Data Loaders"

    def run(self, data=None):
        path = self.config.get("path")
        if not path:
            raise ValueError("Missing 'path' in config.")
        return read_raw_fif(path, preload=True)
