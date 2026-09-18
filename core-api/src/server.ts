import { app } from "./app.js";

const port = Number(process.env.CORE_API_PORT ?? 3001);
if (!Number.isInteger(port) || port < 1 || port > 65535) {
  throw new Error("CORE_API_PORT must be an integer between 1 and 65535.");
}

app.listen(port, "127.0.0.1", (error) => {
  if (error) {
    throw error;
  }
  console.log(`Core API listening on http://127.0.0.1:${port}`);
});
