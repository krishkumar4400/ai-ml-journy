import express from "express";
import cors from "cors";
import healthCheckRouter from "./routes/healthCheck.routes.js";
import userRouter from "./routes/user.routes.js";
import cookieParser from "cookie-parser";
import authRoutes from "./auth/auth.routes.js";
import chatRoutes from "./chats/chats.routes.js";
import messageRoutes from "./messages/messages.routes.js";

const app = express();

// middlewares configuration
app.use(express.json({ limit: "16kb" }));
app.use(express.urlencoded({ extended: true, limit: "16kb" }));
app.use(express.static("public"));
app.use(cookieParser());
// cors configurations
// -----------------------------------
// CORS
// -----------------------------------

app.use(
    cors({

        origin:
            "http://localhost:3000",

        credentials: true,
    })
);

// app.use(
//   cors({
//     origin: process.env.ALLOWED_ORIGIN?.split(",") || "http://localhost:3000",
//     credentials: true,
//     allowedHeaders: ["Authorization", "Content-Type"],
//     methods: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
//   }),
// );

app.get("/", (req, res) => {
  return res.send("Hello Express");
});

// import the routes
app.use("/api/v1/healthcheck", healthCheckRouter);
app.use("/api/v1/auth", userRouter);

app.use("/api/auth", authRoutes);
app.use("/api/chats", chatRoutes);
app.use("/api/messages", messageRoutes);
export default app;
