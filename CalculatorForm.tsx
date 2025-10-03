import React, { useState } from "react";

export default function CalculatorForm({ inputsSchema, onSubmit }: any) {
  const [state, setState] = useState(() => {
    const s: any = {};
    Object.keys(inputsSchema).forEach(k => s[k] = "");
    return s;
  });

  const handleChange = (k: string, v: any) => setState((s: any) => ({ ...s, [k]: v }));

  return (
    <form onSubmit={(e) => { e.preventDefault(); onSubmit(state); }}>
      <div className="grid gap-4 mt-4">
        {Object.entries(inputsSchema).map(([k, spec]: any) => (
          <div key={k}>
            <label className="block text-sm font-medium">{k}</label>
            <input
              aria-label={k}
              name={k}
              value={state[k]}
              onChange={(e) => handleChange(k, e.target.value)}
              className="mt-1 p-2 border rounded w-full"
            />
            {spec.example && <small className="text-xs text-muted">e.g. {spec.example}</small>}
          </div>
        ))}
      </div>
      <div className="mt-4">
        <button className="px-4 py-2 rounded bg-sky-600 text-white" type="submit">Compute</button>
      </div>
    </form>
  );
}
