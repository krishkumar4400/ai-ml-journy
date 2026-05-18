type Props = {
    role: "user" | "assistant";
    content: string;
};

export default function MessageBubble({
    role,
    content,
}: Props) {
    return (
        <div
            className={`
        flex
        ${role === "user"
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
          ${role === "user"
                        ? "bg-white text-black"
                        : "bg-zinc-800 text-white"
                    }
        `}
            >
                {content}
            </div>
        </div>
    );
}