
import React from "react";

type ResultsPanelProps = {
  results: any;
  error: string | null;
};

const ResultsPanel: React.FC<ResultsPanelProps> = ({ results, error }) => {
  return (
    <div className="p-4 bg-white border border-gray-300 rounded shadow-md mt-4 max-h-96 overflow-y-auto">
      <h2 className="text-lg font-semibold mb-2">Execution Results</h2>
      {error ? (
        <div className="text-red-600 font-mono whitespace-pre-wrap">
          <strong>Error:</strong> {error}
        </div>
      ) : (
        <pre className="text-sm font-mono whitespace-pre-wrap text-gray-800">
          {JSON.stringify(results, null, 2)}
        </pre>
      )}
    </div>
  );
};

export default ResultsPanel;
