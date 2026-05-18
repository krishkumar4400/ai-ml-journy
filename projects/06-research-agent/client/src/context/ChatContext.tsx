"use client";

import {

    createContext,

    useContext,

    useState,

} from "react";

type Message = {

    role: "user" | "assistant";

    content: string;
};

type Chat = {

    id: string;

    title: string;
};

type ChatContextType = {

    chats: Chat[];

    setChats: React.Dispatch<
        React.SetStateAction<Chat[]>
    >;

    currentChatId: string;

    setCurrentChatId: (
        id: string
    ) => void;

    messages: Message[];

    setMessages: React.Dispatch<
        React.SetStateAction<Message[]>
    >;
};

const ChatContext =
    createContext<ChatContextType>(
        {} as ChatContextType
    );

export function ChatProvider({

    children,

}: {
    children: React.ReactNode;
}) {

    const [chats, setChats] =
        useState<Chat[]>([]);

    const [messages, setMessages] =
        useState<Message[]>([]);

    const [
        currentChatId,
        setCurrentChatId,
    ] = useState("");

    return (

        <ChatContext.Provider
            value={{

                chats,
                setChats,

                currentChatId,
                setCurrentChatId,

                messages,
                setMessages,
            }}
        >

            {children}

        </ChatContext.Provider>
    );
}

export function useChat() {

    return useContext(
        ChatContext
    );
}