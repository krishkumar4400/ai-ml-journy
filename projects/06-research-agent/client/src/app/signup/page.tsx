"use client";

import {
    useState,
} from "react";

import Link from "next/link";

import {
    useRouter,
} from "next/navigation";

import {
    useAuth,
} from "@/context/AuthContext";

import PublicRoute
    from "@/components/auth/PublicRoute";

export default function SignupPage() {

    // -----------------------------------
    // Hooks
    // -----------------------------------

    const router =
        useRouter();

    const { login } =
        useAuth();

    // -----------------------------------
    // State
    // -----------------------------------

    const [name, setName] =
        useState("");

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState("");

    // -----------------------------------
    // Submit
    // -----------------------------------

    async function handleSignup() {

        try {

            setLoading(true);

            setError("");

            const response =
                await fetch(

                    "http://localhost:4000/api/auth/signup",

                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json",
                        },

                        body: JSON.stringify({

                            name,

                            email,

                            password,
                        }),
                    }
                );

            const data =
                await response.json();

            if (!data.success) {

                throw new Error(
                    data.message ||
                    "Signup failed"
                );
            }

            // -----------------------------------
            // Save Token
            // -----------------------------------

            login(
                data.data.token
            );

            // -----------------------------------
            // Redirect
            // -----------------------------------

            router.push(
                "/chat"
            );

        } catch (error: any) {

            setError(
                error.message
            );

        } finally {

            setLoading(false);
        }
    }

    // -----------------------------------
    // UI
    // -----------------------------------

    return (
<PublicRoute>
        <main
            className="
                min-h-screen
                bg-black
                flex
                items-center
                justify-center
                px-4
            "
        >

            <div
                className="
                    w-full
                    max-w-md
                    bg-zinc-900
                    rounded-3xl
                    p-8
                    space-y-5
                    border
                    border-zinc-800
                "
            >

                {/* Heading */}

                <div
                    className="
                        space-y-2
                    "
                >

                    <h1
                        className="
                            text-4xl
                            font-bold
                            text-white
                        "
                    >
                        Create Account
                    </h1>

                    <p
                        className="
                            text-zinc-400
                        "
                    >
                        Start building with AI 🚀
                    </p>

                </div>

                {/* Error */}

                {error && (

                    <div
                        className="
                            bg-red-500/10
                            border
                            border-red-500/20
                            text-red-400
                            p-3
                            rounded-xl
                            text-sm
                        "
                    >
                        {error}
                    </div>
                )}

                {/* Name */}

                <input
                    type="text"

                    placeholder="Your name"

                    value={name}

                    onChange={(e) =>
                        setName(
                            e.target.value
                        )
                    }

                    className="
                        w-full
                        bg-zinc-800
                        text-white
                        p-4
                        rounded-xl
                        outline-none
                        border
                        border-zinc-700
                        focus:border-blue-500
                    "
                />

                {/* Email */}

                <input
                    type="email"

                    placeholder="Email address"

                    value={email}

                    onChange={(e) =>
                        setEmail(
                            e.target.value
                        )
                    }

                    className="
                        w-full
                        bg-zinc-800
                        text-white
                        p-4
                        rounded-xl
                        outline-none
                        border
                        border-zinc-700
                        focus:border-blue-500
                    "
                />

                {/* Password */}

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
                        bg-zinc-800
                        text-white
                        p-4
                        rounded-xl
                        outline-none
                        border
                        border-zinc-700
                        focus:border-blue-500
                    "
                />

                {/* Button */}

                <button
                    onClick={handleSignup}

                    disabled={loading}

                    className="
                        w-full
                        bg-blue-600
                        hover:bg-blue-700
                        disabled:opacity-50
                        text-white
                        p-4
                        rounded-xl
                        font-medium
                        transition
                    "
                >

                    {loading
                        ? "Creating account..."
                        : "Create Account"}

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
                        href="/login"
                        className="
                            text-blue-400
                            hover:underline
                        "
                    >
                        Login
                    </Link>

                </p>

            </div>

        </main>
        </PublicRoute>
    );
}