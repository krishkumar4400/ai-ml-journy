type Props = {
    agent: string;

    output: string;
};

export default function AgentCard({
    agent,
    output,
}: Props) {
    return (
        <div
            className="
        bg-zinc-900
        border
        border-zinc-800
        rounded-2xl
        p-5
      "
        >
            {/* Agent Name */}

            <div className="flex items-center gap-3 mb-4">
                <div
                    className="
            w-3
            h-3
            rounded-full
            bg-green-400
          "
                />

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