type ModuleItemProps = {
  module: {
    id: string;
    label: string;
  };
};

const ModuleItem = ({ module }: ModuleItemProps) => {
  const handleDragStart = (event: React.DragEvent<HTMLDivElement>) => {
    event.dataTransfer.setData("application/reactflow", JSON.stringify(module));
    event.dataTransfer.effectAllowed = "move";
  };

  return (
    <div
      className="bg-white border border-gray-300 rounded px-2 py-1 text-sm cursor-move shadow-sm hover:bg-gray-50"
      draggable
      onDragStart={handleDragStart}
    >
      {module.label}
    </div>
  );
};

export default ModuleItem;