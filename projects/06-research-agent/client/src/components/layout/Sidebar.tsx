"use client";

import {

    useEffect,

} from "react";

import {

    useChat,

} from "@/context/ChatContext";

import {

    apiFetch,

} from "@/lib/api";

export default function Sidebar() {

    const {

        chats,
        setChats,

        currentChatId,
        setCurrentChatId,

        setMessages,

    } = useChat();

    // -----------------------------------
    // Load Chats
    // -----------------------------------

    useEffect(() => {

        fetchChats();

    }, []);

    async function fetchChats() {

        const response =
            await apiFetch(
                "/api/chats"
            );

        const data =
            await response.json();

        if (data.success) {

            setChats(
                data.data
            );
        }
    }

    // -----------------------------------
    // Open Chat
    // -----------------------------------

    async function openChat(
        chatId: string
    ) {

        setCurrentChatId(
            chatId
        );

        const response =
            await apiFetch(
                `/api/chats/${chatId}`
            );

        const data =
            await response.json();

        if (data.success) {

            setMessages(
                data.data.messages
            );
        }
    }

    return (

        <aside
            className="
                w-72
                border-r
                border-zinc-800
                bg-zinc-950
                p-4
                flex
                flex-col
            "
        >

            {/* New Chat */}

            <button
                className="
                    bg-blue-600
                    hover:bg-blue-700
                    text-white
                    p-3
                    rounded-xl
                    mb-6
                "
            >
                + New Chat
            </button>

            {/* Chat List */}

            <div
                className="
                    flex-1
                    overflow-y-auto
                    space-y-2
                "
            >

                {chats.map(
                    (chat) => (

                        <button
                            key={chat.id}

                            onClick={() =>
                                openChat(
                                    chat.id
                                )
                            }

                            className={`
                                w-full
                                text-left
                                p-3
                                rounded-xl
                                transition

                                ${currentChatId ===
                                    chat.id

                                    ? "bg-zinc-800"

                                    : "hover:bg-zinc-900"
                                }
                            `}
                        >

                            <div
                                className="
                                    text-sm
                                    text-zinc-200
                                    truncate
                                "
                            >
                                {chat.title}
                            </div>

                        </button>
                    )
                )}

            </div>

        </aside>
    );
}