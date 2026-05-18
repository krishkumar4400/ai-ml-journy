"use client";

import {
    useState,
} from "react";

import {
    useRouter,
} from "next/navigation";

import {
    useAuth,
} from "@/context/AuthContext";

import PublicRoute
    from "@/components/auth/PublicRoute";
import Link from "next/link";

export default function LoginPage() {

    const router =
        useRouter();

    const { login } =
        useAuth();

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    async function handleLogin() {

        const response =
            await fetch(

                "http://localhost:4000/api/auth/login",

                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json",
                    },

                    body: JSON.stringify({

                        email,

                        password,
                    }),
                }
            );

        const data =
            await response.json();

        if (data.success) {

            login(
                data.data.token
            );

            router.push(
                "/chat"
            );
        }
    }

    return (
<PublicRoute>
        <main
            className="
                min-h-screen
                bg-black
                flex
                items-center
                justify-center
            "
        >

            <div
                className="
                    bg-zinc-900
                    p-8
                    rounded-2xl
                    w-full
                    max-w-md
                    space-y-4
                "
            >

                <h1
                    className="
                        text-3xl
                        font-bold
                        text-white
                    "
                >
                    Login
                </h1>

                <input
                    placeholder="Email"
                    value={email}
                    onChange={(e) =>
                        setEmail(
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        p-3
                        rounded-xl
                        bg-zinc-800
                        text-white
                    "
                />

                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) =>
                        setPassword(
                            e.target.value
                        )
                    }
                    className="
                        w-full
                        p-3
                        rounded-xl
                        bg-zinc-800
                        text-white
                    "
                />

                <button
                    onClick={handleLogin}
                    className="
                        w-full
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        p-3
                        rounded-xl
                    "
                >
                    Login
                </button>
                    {/* Footer */}

                    <p
                        className="
                        text-zinc-400
                        text-sm
                        text-center
                    "
                    >

                        Already have an account?{" "}

                        <Link
                            href="/signup"
                            className="
                            text-blue-400
                            hover:underline
                        "
                        >
                            signup
                        </Link>

                    </p>
            </div>
           

        </main>
        </PublicRoute>
    );
}