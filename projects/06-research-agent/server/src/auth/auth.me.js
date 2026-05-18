import prisma from "../lib/prisma.js";

import { authMiddleware } from "./auth.middleware.js";
authMiddleware

export async function getMe(req, res) {
  try {
    const userId = req.user?.userId;

    const user = await prisma.user.findUnique({
      where: {
        id: userId,
      },

      select: {
        id: true,

        email: true,

        name: true,

        createdAt: true,
      },
    });

    return res.json({
      success: true,

      data: user,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,
      message: error.message,
    });
  }
}
