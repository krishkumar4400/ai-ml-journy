import AgentCard from "./AgentCard";

type Step = {
    agent: string;

    output: string;
    
    status: string;
};

type Props = {
    steps: Step[];
};

export default function AgentTimeline({
    steps,
}: Props) {
    return (
        <div className="space-y-6 mb-10">
            {steps.map(
                (step, index) => (
                    <AgentCard
                        key={index}

                        agent={step.agent}

                        output={step.output}

                        status={step.status}
                    />
                )
            )}
        </div>
    );
}