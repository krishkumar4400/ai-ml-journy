import { Router } from "express";

import { authMiddleware } from "../auth/auth.middleware.js";

import { sendMessageController } from "./messages.controller.js";

const router = Router();

router.use(authMiddleware);

router.post("/", sendMessageController);

export default router;
