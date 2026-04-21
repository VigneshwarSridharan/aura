"use client";

import { FormEvent, useMemo, useState } from "react";

type ChatApiResponse = {
  response: string;
};

const backendBaseUrl =
  process.env.NEXT_PUBLIC_BACKEND_URL ?? "http://localhost:8000";

export default function Home() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const canSubmit = useMemo(() => message.trim().length > 0 && !loading, [message, loading]);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setReply("");
    setLoading(true);

    try {
      const res = await fetch(`${backendBaseUrl}/api/v1/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
      });

      if (!res.ok) {
        throw new Error(`Backend request failed (${res.status})`);
      }

      const data = (await res.json()) as ChatApiResponse;
      setReply(data.response);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Unexpected error while contacting backend.",
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto flex w-full max-w-3xl flex-col gap-8 px-6 py-12">
        <header className="space-y-2">
          <p className="text-xs uppercase tracking-[0.2em] text-cyan-400">AI Starter</p>
          <h1 className="text-3xl font-semibold">Next.js + FastAPI</h1>
          <p className="text-sm text-slate-300">
            Frontend sends prompts to the Python backend. Replace the backend stub with your
            preferred AI provider.
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="space-y-4 rounded-xl border border-slate-800 bg-slate-900/80 p-5"
        >
          <label className="block text-sm font-medium">Prompt</label>
          <textarea
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            placeholder="Ask anything..."
            className="h-32 w-full rounded-md border border-slate-700 bg-slate-950 p-3 outline-none focus:border-cyan-400"
          />
          <button
            type="submit"
            disabled={!canSubmit}
            className="rounded-md bg-cyan-500 px-4 py-2 font-medium text-slate-950 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? "Thinking..." : "Send to backend"}
          </button>
        </form>

        {error && (
          <section className="rounded-xl border border-red-600/40 bg-red-950/30 p-4">
            <h2 className="text-sm font-semibold text-red-300">Error</h2>
            <p className="mt-2 text-sm text-red-200">{error}</p>
          </section>
        )}

        {reply && (
          <section className="rounded-xl border border-emerald-600/40 bg-emerald-950/30 p-4">
            <h2 className="text-sm font-semibold text-emerald-300">Backend response</h2>
            <p className="mt-2 whitespace-pre-wrap text-sm text-emerald-100">{reply}</p>
          </section>
        )}
      </div>
    </main>
  );
}
