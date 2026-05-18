import {
  askAI,
} from "../ai/ai.service.js";
import axios from "axios";

import {
  saveMessage,
} from "./messages.service.js";

export async function
sendMessageController(
  req,
  res
) {

  try {

    const {
      message,
    } = req.body;

    // -----------------------------------
    // Call FastAPI Stream
    // -----------------------------------

    const response =
      await axios.post(

        "http://backend-ai:8000/chat/stream",

        {
          message,
        },

        {
          responseType:
            "stream",
        }
      );

    // -----------------------------------
    // Streaming Headers
    // -----------------------------------

    res.setHeader(
      "Content-Type",
      "text/plain"
    );

    res.setHeader(
      "Transfer-Encoding",
      "chunked"
    );

    // -----------------------------------
    // Pipe Stream
    // -----------------------------------

    response.data.pipe(res);

  } catch (error) {

    return res.status(500).json({

      success: false,

      message:
        error.message,
    });
  }
}