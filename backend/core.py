import json
import logging
import sys
import importlib
from collections import defaultdict, deque
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class NodeGraphExecutor:
    def __init__(self, nodes: List[Dict[str, Any]], edges: List[Dict[str, str]]):
        self.nodes = {node["id"]: node for node in nodes}
        self.edges = edges
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.execution_order = []
        self.results = {}

    def build_graph(self):
        for edge in self.edges:
            source = edge["source"]
            target = edge["target"]
            self.graph[source].append(target)
            self.in_degree[target] += 1
            if source not in self.in_degree:
                self.in_degree[source] = 0

    def topological_sort(self):
        queue = deque([node_id for node_id in self.nodes if self.in_degree[node_id] == 0])
        while queue:
            current = queue.popleft()
            self.execution_order.append(current)
            for neighbor in self.graph[current]:
                self.in_degree[neighbor] -= 1
                if self.in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(self.execution_order) != len(self.nodes):
            raise ValueError("Cycle detected in the node graph")

    def load_node_class(self, node_type: str):
        module_name = node_type.lower().replace("node", "")
        class_name = node_type
        try:
            module = importlib.import_module(f"backend.nodes.{module_name}")
            cls = getattr(module, class_name)
            return cls
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Could not load node class '{class_name}' from module '{module_name}': {e}")

    def execute(self):
        self.build_graph()
        self.topological_sort()

        for node_id in self.execution_order:
            node_info = self.nodes[node_id]
            node_type = node_info["type"]
            config = node_info.get("config", {})

            cls = self.load_node_class(node_type)
            node_instance = cls(config)

            # Gather inputs from upstream nodes
            input_data = []
            for edge in self.edges:
                if edge["target"] == node_id:
                    input_data.append(self.results[edge["source"]])

            logger.info(f"Executing node {node_id} ({node_type}) with config {config}")
            output = node_instance.run(*input_data)
            self.results[node_id] = output

        return self.results


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m backend.core '<json_string>'")
        sys.exit(1)

    try:
        graph = json.loads(sys.argv[1])
        nodes = graph.get("nodes", [])
        edges = graph.get("edges", [])

        executor = NodeGraphExecutor(nodes, edges)
        results = executor.execute()

        print(json.dumps({"status": "success", "results": list(results.keys())}, indent=2))

    except Exception as e:
        logger.exception("Error executing node graph")
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
