import NodeCanvas from "./components/NodeCanvas";
import Sidebar from "./components/Sidebar";

function App() {
  
  return (  
    <div className="flex h-screen">
      <Sidebar />
      <NodeCanvas />
    </div>

  );
}

export default App;
