import "dotenv/config";
import app from "./src/app.js";
import http from "http";
import connectToDB from "./src/db/index.js";

const port = process.env.PORT || 4001;

await connectToDB();

const server = http.createServer(app);

server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
