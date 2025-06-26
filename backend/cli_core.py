import json
import os
from backend.nodes.registry import NODE_REGISTRY, discover_nodes
# from nodes.registry import NODE_REGISTRY, discover_nodes

# Discover and register all nodes in the nodes directory
nodes_dir = os.path.join(os.path.dirname(__file__), "nodes")
discover_nodes(nodes_dir)

def run_pipeline(pipeline_config):
    """
    Run a sequence of nodes defined in the pipeline_config.
    Each node receives the output of the previous node.
    """
    data = None
    for node_cfg in pipeline_config:
        node_type = node_cfg.get("type")
        config = node_cfg.get("config", {})

        if node_type not in NODE_REGISTRY:
            raise ValueError(f"Unknown node type: {node_type}")

        node_class = NODE_REGISTRY[node_type]
        node_instance = node_class(config=config)
        data = node_instance.run(data)

    return data

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python core.py '<pipeline_json>'")
        sys.exit(1)
        # EXAMPLE: python -m backend.core '[{"type": "LoadDataNode", "config": {"path": "./data/MNE-sample-data/MEG/sample/sample_audvis_raw.fif"}}, {"type": "BandpassFilterNode", "config": {"l_freq": 1.0, "h_freq": 40.0}}]'

    pipeline_json = sys.argv[1]
    pipeline_config = json.loads(pipeline_json)

    result = run_pipeline(pipeline_config)

    # For demonstration, just print the type of result
    print(f"Pipeline executed. Final result type: {type(result)}")

