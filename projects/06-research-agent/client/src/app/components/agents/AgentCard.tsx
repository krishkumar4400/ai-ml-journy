type Props = {
    agent: string;

    output: string;

    status?: string;
};

export default function AgentCard({
    agent,
    output,
    status,
}: Props) {
    return (
        <div
            className="
        bg-zinc-900
        border
        border-zinc-800
        rounded-2xl
        p-5
        animate-in
        fade-in
        slide-in-from-bottom-4
      "
        >
            {/* Header */}

            <div className="flex items-center gap-3 mb-4">
                {/* Status */}

                <div
                    className={`
            w-3
            h-3
            rounded-full

            ${status ===
                            "completed"
                            ? "bg-green-400"
                            : "bg-yellow-400 animate-pulse"
                        }
          `}
                />

                {/* Agent Name */}

                <h3 className="text-xl font-bold">
                    {agent}
                </h3>
            </div>

            {/* Output */}

            <p
                className="
          text-zinc-300
          whitespace-pre-wrap
        "
            >
                {output}
            </p>
        </div>
    );
}