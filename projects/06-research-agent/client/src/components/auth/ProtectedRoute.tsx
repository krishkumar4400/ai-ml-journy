"use client";

import {
    useEffect,
} from "react";

import {
    useRouter,
} from "next/navigation";

import {
    useAuth,
} from "@/context/AuthContext";

export default function ProtectedRoute({

    children,

}: {
    children: React.ReactNode;
}) {

    const router =
        useRouter();

    const {
        user,
        loading,
    } = useAuth();

    // -----------------------------------
    // Redirect
    // -----------------------------------

    useEffect(() => {

        if (
            !loading &&
            !user
        ) {

            router.push(
                "/login"
            );
        }

    }, [
        user,
        loading,
        router,
    ]);

    // -----------------------------------
    // Loading Screen
    // -----------------------------------

    if (loading) {

        return (

            <main
                className="
                    min-h-screen
                    bg-black
                    text-white
                    flex
                    items-center
                    justify-center
                "
            >

                <div
                    className="
                        animate-pulse
                        text-zinc-400
                    "
                >
                    Loading...
                </div>

            </main>
        );
    }

    // -----------------------------------
    // Prevent flash
    // -----------------------------------

    if (!user) {
        return null;
    }

    return children;
}