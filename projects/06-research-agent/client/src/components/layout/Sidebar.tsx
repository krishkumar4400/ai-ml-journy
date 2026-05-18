
import {
    useAuth,
} from "@/context/AuthContext";

export default function Sidebar() {
    const {
        user,
        logout,
    } = useAuth();
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
            <div
                className="
        mt-auto
        pt-4
        border-t
        border-zinc-800
    "
            >

                <div
                    className="
            text-sm
            text-zinc-400
            mb-3
        "
                >
                    {user?.email}
                </div>

                <button
                    onClick={logout}
                    className="
            w-full
            bg-red-500/10
            hover:bg-red-500/20
            text-red-400
            p-3
            rounded-xl
            transition
        "
                >
                    Logout
                </button>

            </div>
        </aside>
    );
}