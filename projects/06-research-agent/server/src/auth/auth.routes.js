import { Router } from "express";

import { signup, login } from "./auth.controller.js";

import { authMiddleware } from "./auth.middleware.js";

import { getMe } from "./auth.me.js";

const router = Router();

router.post("/signup", signup);

router.post("/login", login);

router.get(
  "/me",

  authMiddleware,

  getMe,
);

export default router;
