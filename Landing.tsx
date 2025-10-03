import React, { useEffect, useState } from "react";
import { listModules } from "../utils/api";
import { Link } from "react-router-dom";

export default function Landing(){
  const [modules, setModules] = useState<any>({});
  useEffect(()=> {
    listModules().then(d => setModules(d.modules || {})).catch(()=>{});
  },[]);
  return (
    <div>
      <h2 className="text-2xl font-semibold">Calculators</h2>
      <div className="grid gap-3 mt-4">
        {Object.entries(modules).length === 0 && <div>No modules (backend maybe not running)</div>}
        {Object.entries(modules).map(([k, v]: any) => (
          <Link key={k} to={`/calculator/${k}`} className="p-3 border rounded hover:shadow">
            <div className="flex justify-between">
              <div>
                <div className="font-medium">{v.title}</div>
                <div className="text-sm text-muted">{v.description}</div>
              </div>
              <div className="text-xs text-gray-500">{k}</div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
