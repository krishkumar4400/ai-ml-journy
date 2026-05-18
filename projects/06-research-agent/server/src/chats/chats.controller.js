import { authMiddleware } from "../auth/auth.middleware.js";

import { createChat, getUserChats, getChatById } from "./chats.service.js";

export async function createChatController(
  req,

  res,
) {
  try {
    const userId = req.user?.userId;

    const { title } = req.body;

    const chat = await createChat(title, userId);

    return res.json({
      success: true,

      data: chat,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,

      message: error.message,
    });
  }
}

export async function getChatsController(
  req,

  res,
) {
  try {
    const userId = req.user?.userId;

    const chats = await getUserChats(userId);

    return res.json({
      success: true,

      data: chats,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,

      message: error.message,
    });
  }
}

export async function getChatController(
  req,

  res,
) {
  try {
    const userId = req.user?.userId;

    const { id } = req.params;

    const chat = await getChatById(id, userId);

    return res.json({
      success: true,

      data: chat,
    });
  } catch (error) {
    return res.status(500).json({
      success: false,

      message: error.message,
    });
  }
}
