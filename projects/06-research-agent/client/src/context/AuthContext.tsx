"use client";

import {

    createContext,

    useContext,

    useEffect,

    useState,

} from "react";

type User = {

    id: string;

    email: string;

    name?: string;
};

type AuthContextType = {

    user: User | null;

    loading: boolean;

    login: (
        token: string
    ) => void;

    logout: () => void;
};

const AuthContext =
    createContext<AuthContextType>(
        {} as AuthContextType
    );

export function AuthProvider({

    children,

}: {
    children: React.ReactNode;
}) {

    const [user, setUser] =
        useState<User | null>(null);

    const [loading, setLoading] =
        useState(true);

    // -----------------------------------
    // Load Current User
    // -----------------------------------

    useEffect(() => {

        const token =
            localStorage.getItem(
                "token"
            );

        if (!token) {

            setLoading(false);

            return;
        }

        fetchCurrentUser();

    }, []);

    // -----------------------------------
    // Fetch User
    // -----------------------------------

    async function fetchCurrentUser() {

        try {

            const response =
                await fetch(

                    "http://localhost:4000/api/auth/me",

                    {
                        headers: {
                            Authorization:
                                `Bearer ${localStorage.getItem("token")}`,
                        },
                    }
                );

            const data =
                await response.json();

            if (data.success) {

                setUser(data.data);
            }

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);
        }
    }

    // -----------------------------------
    // Login
    // -----------------------------------

    function login(
        token: string
    ) {

        localStorage.setItem(
            "token",
            token
        );

        fetchCurrentUser();
    }

    // -----------------------------------
    // Logout
    // -----------------------------------

    function logout() {

        localStorage.removeItem(
            "token"
        );

        setUser(null);
    }

    return (

        <AuthContext.Provider
            value={{

                user,

                loading,

                login,

                logout,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {

    return useContext(
        AuthContext
    );
}