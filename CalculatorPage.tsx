import React, { useEffect, useState } from "react";
import { execModule, listModules } from "../utils/api";
import CalculatorForm from "../components/CalculatorForm";
import ResultCard from "../components/ResultCard";
import { useParams } from "react-router-dom";

export default function CalculatorPage() {
  const { module } = useParams();
  const [meta, setMeta] = useState<any>(null);
  const [result, setResult] = useState<any>(null);

  useEffect(() => {
    listModules().then(d => {
      if (module) setMeta(d.modules[module]);
    }).catch(()=>{});
  }, [module]);

  async function onSubmit(inputs: any) {
    if (!module) return;
    const res = await execModule(module, inputs);
    setResult(res);
  }

  if (!meta) return <div>Loading...</div>;

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-semibold">{meta.title}</h1>
      <p className="text-sm text-muted">{meta.description}</p>

      <CalculatorForm inputsSchema={meta.inputs} onSubmit={onSubmit} />
      {result && <ResultCard data={result} />}
    </div>
  );
}
