"use client";

import { useEffect, useState } from "react";

import Sidebar from "@/components/layout/Sidebar";

import ChatInput from "@/components/chat/ChatInput";

import ChatWindow from "@/components/chat/ChatWindow";
import ProtectedRoute
    from "@/components/auth/ProtectedRoute";

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
    // Token
    // -----------------------------------

    const [token, setToken] =
        useState("");

    useEffect(() => {

        const storedToken =
            localStorage.getItem(
                "token"
            );

        if (storedToken) {
            setToken(storedToken);
        }

    }, []);

    // -----------------------------------
    // Send Message
    // -----------------------------------

    const sendMessage =
        async () => {

            if (!input.trim()) return;

            setLoading(true);

            // -----------------------------------
            // Store current input
            // -----------------------------------

            const userMessage =
                input;

            // -----------------------------------
            // Add User Message
            // -----------------------------------

            setMessages(prev => [
                ...prev,

                {
                    role: "user",
                    content: userMessage,
                },

                // Assistant placeholder
                {
                    role: "assistant",
                    content: "",
                },
            ]);

            // -----------------------------------
            // Clear input
            // -----------------------------------

            setInput("");

            try {

                const response =
                    await fetch(
                        "http://localhost:4000/api/messages",

                        {
                            method: "POST",

                            headers: {
                                "Content-Type":
                                    "application/json",

                                Authorization:
                                    `Bearer ${token}`,
                            },

                            body: JSON.stringify({
                                message: userMessage,
                            }),
                        }
                    );

                // -----------------------------------
                // Stream Reader
                // -----------------------------------

                const reader =
                    response.body?.getReader();

                if (!reader) {
                    throw new Error(
                        "No response body"
                    );
                }

                const decoder =
                    new TextDecoder();

                let finalText = "";

                // -----------------------------------
                // Read Stream
                // -----------------------------------

                while (true) {

                    const {
                        done,
                        value,
                    } = await reader.read();

                    if (done) break;

                    const chunk =
                        decoder.decode(value);

                    finalText += chunk;

                    // -----------------------------------
                    // Update LAST assistant message
                    // -----------------------------------

                    setMessages(prev => {

                        const updated =
                            [...prev];

                        updated[
                            updated.length - 1
                        ] = {
                            role: "assistant",
                            content: finalText,
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
        <ProtectedRoute>
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
        </ProtectedRoute>
    );
}