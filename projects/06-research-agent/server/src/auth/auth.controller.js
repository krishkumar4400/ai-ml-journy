

import {
    signupSchema,
    loginSchema,
} from "./auth.validation.js";

import {
    signupUser,
    loginUser,
} from "./auth.service.js";

export async function signup(
    req,
    res
) {

    try {

        const body =
            signupSchema.parse(
                req.body
            );

        const result =
            await signupUser(
                body.email,
                body.password,
                body.name
            );

        return res.json({
            success: true,
            data: result,
        });

    } catch (error) {

        return res.status(400).json({
            success: false,
            message:
                error.message,
        });
    }
}

export async function login(
    req,
    res
) {

    try {

        const body =
            loginSchema.parse(
                req.body
            );

        const result =
            await loginUser(
                body.email,
                body.password
            );

        return res.json({
            success: true,
            data: result,
        });

    } catch (error) {

        return res.status(400).json({
            success: false,
            message:
                error.message,
        });
    }
}