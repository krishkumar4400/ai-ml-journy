type Source = {
    content: string;

    metadata?: Record<
        string,
        any
    >;
};

type Props = {
    sources: Source[];
};

export default function SourceViewer({
    sources,
}: Props) {
    return (
        <div className="mt-6">
            <h3 className="text-xl font-bold mb-4">
                Sources
            </h3>

            <div className="space-y-4">
                {sources.map(
                    (source, index) => (
                        <div
                            key={index}
                            className="
                bg-zinc-900
                border
                border-zinc-800
                rounded-xl
                p-4
              "
                        >
                            <p
                                className="
                  text-zinc-300
                  whitespace-pre-wrap
                "
                            >
                                {source.content}
                            </p>
                        </div>
                    )
                )}
            </div>
        </div>
    );
}