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

export default function PublicRoute({

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

    useEffect(() => {

        if (
            !loading &&
            user
        ) {

            router.push(
                "/chat"
            );
        }

    }, [
        user,
        loading,
        router,
    ]);

    if (loading) {

        return (

            <main
                className="
                    min-h-screen
                    bg-black
                    flex
                    items-center
                    justify-center
                    text-white
                "
            >
                Loading...
            </main>
        );
    }

    return children;
}