"use client";

import { useState } from "react";

import Sidebar from "@/components/layout/Sidebar";

import PDFUploader from "@/components/upload/PDFUploader";

import PDFChatInput from "@/components/pdf-chat/PDFChatInput";

import PDFChatWindow from "@/components/pdf-chat/PDFChatWindow";
import SourceViewer from "@/components/pdf-chat/SourceViewer";
import TracePanel from "@/components/chat/TracePanel";

type Message = {
    role: "user" | "assistant";

    content: string;

    sources?: {
        content: string;
    }[];
};

export default function PDFChatPage() {
    // -----------------------------------
    // State
    // -----------------------------------

    const [messages, setMessages] =
        useState<Message[]>([]);

    const [input, setInput] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [traces, setTraces] =
        useState<string[]>([]);

    // -----------------------------------
    // Send Question
    // -----------------------------------

    const sendQuestion = async () => {
        if (!input.trim()) return;

        setTraces([]);

        const userMessage = {
            role: "user" as const,
            content: input,
        };

        setMessages((prev) => [
            ...prev,
            userMessage,
        ]);

        setInput("");

        setLoading(true);

        try {
            const response = await fetch(
                "http://127.0.0.1:8000/chat-pdf-stream/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json",
                    },

                    body: JSON.stringify({
                        session_id:
                            "krish-session",

                        question: input,
                    }),
                }
            );

            if (!response.body) return;

            const reader =
                response.body.getReader();

            const decoder =
                new TextDecoder();

            let aiMessage = "";

            // Empty assistant bubble

            setMessages((prev) => [
                ...prev,
                {
                    role: "assistant",
                    content: "",
                },
            ]);

            let done = false;

            while (!done) {
                const result =
                    await reader.read();

                done = result.done;

                const chunk =
                    decoder.decode(result.value);

                const lines =
                    chunk.split("\n");

                for (const line of lines) {
                    if (!line.trim()) continue;

                    try {
                        const parsed =
                            JSON.parse(line);

                        // -----------------------------------
                        // Trace Event
                        // -----------------------------------

                        if (
                            parsed.type === "trace"
                        ) {
                            setTraces((prev) => [
                                ...prev,
                                parsed.message,
                            ]);
                        }

                        // -----------------------------------
                        // Token Event
                        // -----------------------------------

                        if (
                            parsed.type === "token"
                        ) {
                            aiMessage +=
                                parsed.content;

                            setMessages((prev) => {
                                const updated = [
                                    ...prev,
                                ];

                                updated[
                                    updated.length - 1
                                ] = {
                                    role: "assistant",
                                    content: aiMessage,
                                };

                                return updated;
                            });
                        }
                    } catch (err) {
                        console.error(err);
                    }
                }

                setMessages((prev) => {
                    const updated = [
                        ...prev,
                    ];

                    updated[
                        updated.length - 1
                    ] = {
                        role: "assistant",
                        content: aiMessage,
                    };

                    return updated;
                });
            }
        } catch (error) {
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    // -----------------------------------
    // UI
    // -----------------------------------

    return (
        <main
            className="
        h-screen
        bg-black
        text-white
        flex
      "
        >
            {/* Sidebar */}

            <Sidebar />

            {/* Main */}

            <section
                className="
          flex-1
          flex
          flex-col
          p-6
        "
            >
                {/* Upload */}

                <PDFUploader />

                {/* Chat */}
                <TracePanel traces={traces} />
                <PDFChatWindow
                    messages={messages}
                />

                {/* Input */}

                <PDFChatInput
                    value={input}
                    onChange={setInput}
                    onSend={sendQuestion}
                    loading={loading}
                />
            </section>
        </main>
    );
}