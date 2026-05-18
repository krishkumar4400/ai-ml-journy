type Props = {
    value: string;
    onChange: (
        value: string
    ) => void;
    onSend: () => void;
    loading: boolean;
};

export default function ChatInput({
    value,
    onChange,
    onSend,
    loading,
}: Props) {
    return (
        <div className="flex gap-4">
            <input
                type="text"
                placeholder="Ask anything..."
                value={value}
                onChange={(e) =>
                    onChange(e.target.value)
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
        "
            />

            <button
                onClick={onSend}
                disabled={loading}
                className="
          bg-white
          text-black
          px-6
          rounded-xl
          font-semibold
        "
            >
                {loading
                    ? "Thinking..."
                    : "Send"}
            </button>
        </div>
    );
}