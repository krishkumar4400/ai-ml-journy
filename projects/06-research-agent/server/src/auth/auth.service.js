import bcrypt from "bcryptjs";

import jwt from "jsonwebtoken";

import prisma from "../lib/prisma.js";

const JWT_SECRET =
    process.env.JWT_SECRET;

export async function signupUser(
    email,
    password,
    name
) {

    const existingUser =
        await prisma.user.findUnique({
            where: { email },
        });

    if (existingUser) {
        throw new Error(
            "User already exists"
        );
    }

    const hashedPassword =
        await bcrypt.hash(
            password,
            10
        );

    const user =
        await prisma.user.create({
            data: {

                email,

                password:
                    hashedPassword,

                name,
            },
        });

    const token =
        jwt.sign(
            { userId: user.id },
            JWT_SECRET,
            {
                expiresIn: "7d",
            }
        );

    return {
        token,
        user,
    };
}

export async function loginUser(
    email,
    password
) {

    const user =
        await prisma.user.findUnique({
            where: { email },
        });

    if (!user) {
        throw new Error(
            "Invalid credentials"
        );
    }

    const isPasswordValid =
        await bcrypt.compare(
            password,
            user.password
        );

    if (!isPasswordValid) {
        throw new Error(
            "Invalid credentials"
        );
    }

    const token =
        jwt.sign(
            { userId: user.id },
            JWT_SECRET,
            {
                expiresIn: "7d",
            }
        );

    return {
        token,
        user,
    };
}