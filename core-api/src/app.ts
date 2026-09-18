import express from "express";

export const app = express();
app.disable("x-powered-by");

app.get("/health", (_request, response) => {
  response.json({ service: "core-api", status: "ok" });
});
