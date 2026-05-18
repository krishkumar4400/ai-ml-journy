export default function Sidebar() {
    return (
        <aside
            className="
        w-72
        bg-zinc-950
        border-r
        border-zinc-800
        p-4
        flex
        flex-col
      "
        >
            {/* Logo */}

            <h1 className="text-2xl font-bold mb-8">
                AI Agent
            </h1>

            {/* New Chat Button */}

            <button
                className="
          bg-white
          text-black
          rounded-xl
          py-3
          font-semibold
          mb-6
        "
            >
                + New Chat
            </button>

            {/* Chat List */}

            <div className="space-y-2">
                <div
                    className="
            bg-zinc-900
            p-3
            rounded-xl
            cursor-pointer
            hover:bg-zinc-800
          "
                >
                    Future of AI
                </div>

                <div
                    className="
            bg-zinc-900
            p-3
            rounded-xl
            cursor-pointer
            hover:bg-zinc-800
          "
                >
                    Multi-Agent Systems
                </div>
            </div>
        </aside>
    );
}