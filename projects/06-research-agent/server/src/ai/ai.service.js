import axios
from "axios";

const AI_BASE_URL =
  "http://backend-ai:8000";

export async function askAI(
  message
) {

  try {

    const response =
      await axios.post(

        `${AI_BASE_URL}/research`,

        {
          topic: message,
        }
      );

    return response.data;

  } catch (error) {

    console.error(
      error.message
    );

    throw new Error(
      "AI service failed"
    );
  }
}