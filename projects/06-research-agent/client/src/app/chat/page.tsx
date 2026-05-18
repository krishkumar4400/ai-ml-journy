"use client";

import { useState } from "react";

import Sidebar from "@/components/layout/Sidebar";

import ChatInput from "@/components/chat/ChatInput";

import ChatWindow from "@/components/chat/ChatWindow";

type Message = {
    role: "user" | "assistant";
    content: string;
};

export default function ChatPage() {
    // -----------------------------------
    // State
    // -----------------------------------

    const [messages, setMessages] =
        useState<Message[]>([]);

    const [input, setInput] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    // -----------------------------------
    // Send Message
    // -----------------------------------

    const sendMessage =
        async () => {
            if (!input.trim()) return;

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
                    "http://127.0.0.1:8000/stream/",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json",
                        },

                        body: JSON.stringify({
                            topic: input,
                        }),
                    }
                );

                if (!response.body) return;

                const reader =
                    response.body.getReader();

                const decoder =
                    new TextDecoder();

                let aiMessage = "";

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
                        decoder.decode(
                            result.value
                        );

                    aiMessage += chunk;

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

            {/* Main Chat */}

            <section
                className="
          flex-1
          flex
          flex-col
          p-6
        "
            >
                {/* Messages */}

                <ChatWindow
                    messages={messages}
                />

                {/* Input */}

                <ChatInput
                    value={input}
                    onChange={setInput}
                    onSend={sendMessage}
                    loading={loading}
                />
            </section>
        </main>
    );
}