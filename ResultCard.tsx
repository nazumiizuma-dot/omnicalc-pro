import React from "react";

export default function ResultCard({ data }: any) {
  return (
    <div className="mt-6 p-4 border rounded bg-white/5">
      <pre className="whitespace-pre-wrap">{JSON.stringify(data, null, 2)}</pre>
      <div className="mt-2 flex gap-2">
        <button className="px-3 py-1 border rounded">Copy</button>
        <button className="px-3 py-1 border rounded">Export PDF</button>
      </div>
    </div>
  );
}
