import { Hono } from "hono";
import { cors } from "hono/cors";
import { router as authRouter } from "./apps/auth/controller";
import { bearerAuth } from "hono/bearer-auth";

const app = new Hono();

const api = new Hono();

app.use("*", cors());

api.route("/auth", authRouter);

app.use("/api", bearerAuth({ token: "TOKEN" }));

app.route("/api", api);

app.get("/", (c) => {
  return c.json({
    message: "it works",
  })
});

export default app;
