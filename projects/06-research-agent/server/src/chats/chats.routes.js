import { Router } from "express";

import { authMiddleware } from "../auth/auth.middleware.js";

import {
  createChatController,
  getChatsController,
  getChatController,
} from "./chats.controller.js";

const router = Router();

router.use(authMiddleware);

router.post("/", createChatController);

router.get("/", getChatsController);

router.get("/:id", getChatController);

export default router;
