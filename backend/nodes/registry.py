NODE_REGISTRY = {}

def register_node(cls):
    NODE_REGISTRY[cls.name()] = cls
    return cls

def discover_nodes(directory):
    import os, importlib.util
    for filename in os.listdir(directory):
        if filename.endswith(".py") and filename not in ("__init__.py", "base.py", "registry.py"):
            module_name = filename[:-3]
            module_path = os.path.join(directory, filename)
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
