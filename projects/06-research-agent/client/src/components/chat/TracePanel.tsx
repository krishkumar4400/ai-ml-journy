type Props = {
    traces: string[];
};

export default function TracePanel({
    traces,
}: Props) {
    return (
        <div
            className="
        bg-zinc-950
        border
        border-zinc-800
        rounded-2xl
        p-5
        mb-6
      "
        >
            <h2 className="text-xl font-bold mb-4">
                Agent Activity
            </h2>

            <div className="space-y-3">
                {traces.map(
                    (trace, index) => (
                        <div
                            key={index}
                            className="
                text-zinc-300
                flex
                items-center
                gap-3
              "
                        >
                            <span className="text-green-400">
                                ✓
                            </span>

                            <span>{trace}</span>
                        </div>
                    )
                )}
            </div>
        </div>
    );
}