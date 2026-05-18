import MessageBubble
    from "./MessageBubble";

type Message = {
    role: "user" | "assistant";
    content: string;
};

type Props = {
    messages: Message[];
};

export default function ChatWindow({
    messages,
}: Props) {

    return (

        <div
            className="
                flex-1
                overflow-y-auto
                space-y-4
                pb-6
            "
        >

            {messages.map(
                (message, index) => (

                    <MessageBubble
                        key={index}
                        role={message.role}
                        content={message.content}
                    />
                )
            )}

        </div>
    );
}