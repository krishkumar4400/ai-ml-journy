"use client";

import { useState } from "react";

import AgentTimeline from "@/components/agents/AgentTimeline";

type Step = {
    agent: string;
    output: string;
    status?: string;
};

export default function ResearchPage() {
    // -----------------------------------
    // State
    // -----------------------------------

    const [topic, setTopic] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [steps, setSteps] =
        useState<Step[]>([]);

    // -----------------------------------
    // Generate Research
    // -----------------------------------

    const generateResearch =
        async () => {
            if (!topic.trim()) return;

            try {
                setLoading(true);

                setSteps([]);

                const response = await fetch(
                    "http://127.0.0.1:8000/multi-agent-stream/",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json",
                        },

                        body: JSON.stringify({
                            topic,
                        }),
                    }
                );

                if (!response.body) return;

                const reader =
                    response.body.getReader();

                const decoder =
                    new TextDecoder();

                let done = false;

                while (!done) {
                    const result =
                        await reader.read();

                    done = result.done;

                    const chunk =
                        decoder.decode(
                            result.value
                        );

                    const lines =
                        chunk.split("\n");

                    for (const line of lines) {
                        if (!line.trim())
                            continue;

                        try {
                            const parsed =
                                JSON.parse(line);

                            // -----------------------------------
                            // Agent Output
                            // -----------------------------------

                            if (
                                parsed.type ===
                                "agent"
                            ) {
                                setSteps((prev) => [
                                    ...prev,
                                    {
                                        agent:
                                            parsed.agent,

                                        output:
                                            parsed.output,

                                        status:
                                            "completed",
                                    },
                                ]);
                            }
                            if (
                                parsed.type ===
                                "status"
                            ) {

                                setSteps((prev) => [

                                    ...prev,

                                    {
                                        agent:
                                            parsed.agent,

                                        output:
                                            parsed.message,

                                        status:
                                            "running",
                                    },
                                ]);
                            }
                        } catch (err) {
                            console.error(err);
                        }
                    }
                }
            } catch (error) {
                console.error(error);

                alert(
                    "Research generation failed"
                );
            } finally {
                setLoading(false);
            }
        };

    // -----------------------------------
    // UI
    // -----------------------------------

    return (
        <main className="min-h-screen bg-black text-white p-8">
            <div className="max-w-6xl mx-auto">
                {/* ----------------------------------- */}
                {/* Heading */}
                {/* ----------------------------------- */}

                <h1 className="text-5xl font-bold mb-2">
                    Multi-Agent Research System
                </h1>

                <p className="text-zinc-400 mb-10">
                    Planner → Researcher → Writer → Critic
                </p>

                {/* ----------------------------------- */}
                {/* Input */}
                {/* ----------------------------------- */}

                <div className="flex gap-4 mb-10">
                    <input
                        type="text"
                        placeholder="Enter research topic..."
                        value={topic}
                        onChange={(e) =>
                            setTopic(
                                e.target.value
                            )
                        }
                        className="
              flex-1
              bg-zinc-900
              border
              border-zinc-700
              rounded-xl
              px-5
              py-4
              outline-none
              text-lg
            "
                    />

                    <button
                        onClick={
                            generateResearch
                        }
                        disabled={loading}
                        className="
              bg-white
              text-black
              px-6
              py-4
              rounded-xl
              font-semibold
              hover:opacity-80
              transition
            "
                    >
                        {loading
                            ? "Running Agents..."
                            : "Generate"}
                    </button>
                </div>

                {/* ----------------------------------- */}
                {/* Agent Timeline */}
                {/* ----------------------------------- */}

                {steps.length > 0 ? (
                    <AgentTimeline
                        steps={steps}
                    />
                ) : (
                    <div
                        className="
              bg-zinc-900
              border
              border-zinc-800
              rounded-2xl
              p-10
              text-zinc-500
            "
                    >
                        Multi-agent workflow
                        will appear here...
                    </div>
                )}
            </div>
        </main>
    );
}