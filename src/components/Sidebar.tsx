import { modules } from "../data/modules";
import ModuleItem from "./ModuleItem";

type Module = {
  id: string;
  label: string;
};

const Sidebar = () => {
  return (
    <div className="w-64 bg-gray-100 p-4 border-r border-gray-300 overflow-y-auto">
      <h2 className="text-lg font-semibold mb-4">Modules</h2>
      {Object.entries(modules).map(([category, items]) => (
        <div key={category} className="mb-6">
          <h3 className="text-sm font-bold text-gray-700 mb-2">{category}</h3>
          <div className="space-y-2">
            {(items as Module[]).map((item) => (
              <ModuleItem key={item.id} module={item} />
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default Sidebar;
