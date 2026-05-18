"use client";

import ReactMarkdown
    from "react-markdown";

import remarkGfm
    from "remark-gfm";

import {
    Prism as SyntaxHighlighter,
} from "react-syntax-highlighter";

import {
    oneDark,
} from "react-syntax-highlighter/dist/esm/styles/prism";

type Props = {
    role: "user" | "assistant";

    content: string;
};

export default function MessageBubble({

    role,

    content,

}: Props) {

    const isUser =
        role === "user";

    return (

        <div
            className={`
                w-full
                flex
                ${isUser
                    ? "justify-end"
                    : "justify-start"}
            `}
        >

            <div
                className={`
                    max-w-3xl
                    rounded-2xl
                    px-4
                    py-3
                    whitespace-pre-wrap
                    text-sm
                    leading-7

                    ${isUser
                        ? "bg-blue-600 text-white"
                        : "bg-zinc-900 text-zinc-100"}
                `}
            >

                <ReactMarkdown

                    remarkPlugins={[
                        remarkGfm,
                    ]}

                    components={{

                        code({
                            inline,
                            className,
                            children,
                            ...props
                        }: any) {

                            const match =
                                /language-(\w+)/.exec(
                                    className || ""
                                );

                            return !inline &&
                                match ? (

                                <SyntaxHighlighter

                                    style={oneDark}

                                    language={match[1]}

                                    PreTag="div"

                                    customStyle={{
                                        borderRadius:
                                            "12px",

                                        padding:
                                            "16px",

                                        fontSize:
                                            "14px",
                                    }}

                                    {...props}
                                >
                                    {String(
                                        children
                                    ).replace(/\n$/, "")}
                                </SyntaxHighlighter>

                            ) : (

                                <code
                                    className="
                                        bg-zinc-800
                                        px-1
                                        py-0.5
                                        rounded
                                    "
                                    {...props}
                                >
                                    {children}
                                </code>
                            );
                        },
                    }}

                >
                    {content}
                </ReactMarkdown>

            </div>

        </div>
    );
}