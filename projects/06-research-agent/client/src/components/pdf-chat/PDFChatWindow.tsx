import SourceViewer from "./SourceViewer";

type Message = {
    role: "user" | "assistant";

    content: string;

    sources?: {
        content: string;
    }[];
};

type Props = {
    messages: Message[];
};

export default function PDFChatWindow({
    messages,
}: Props) {
    return (
        <div
            className="
        flex-1
        overflow-y-auto
        space-y-6
        mb-6
      "
        >
            {messages.map(
                (message, index) => (
                    <div key={index}>
                        {/* Bubble */}

                        <div
                            className={`
                flex
                ${message.role ===
                                    "user"
                                    ? "justify-end"
                                    : "justify-start"
                                }
              `}
                        >
                            <div
                                className={`
                  max-w-3xl
                  px-5
                  py-4
                  rounded-2xl
                  whitespace-pre-wrap
                  ${message.role ===
                                        "user"
                                        ? "bg-white text-black"
                                        : "bg-zinc-800 text-white"
                                    }
                `}
                            >
                                {message.content}
                            </div>
                        </div>

                        {/* Sources */}

                        {message.sources &&
                            message.sources.length >
                            0 && (
                                <SourceViewer
                                    sources={
                                        message.sources
                                    }
                                />
                            )}
                    </div>
                )
            )}
        </div>
    );
}