import { Hono } from "hono";
import { decode, jwt, sign, verify } from "hono/jwt";

export const router = new Hono();

const users = [
  {
    name: "Soham",
    email: "soham@gmail.com",
    password: "Hello@123",
  },
  {
    name: "Sandip",
    email: "sandip@gmail.com",
    password: "Hello@123",
  },
];

router.post("/login", async (c) => {
  const body = await c.req.json();

  console.log(body);

  // check if user exists and check if password is correct
  const user = users.find((u) => u.email === body.email);

  if (!user || user.password !== body.password) {
    return c.json(
      {
        message: "Email or password is incorrect",
      },
      401
    );
  }

  // return jwt token
  const token = await sign({ email: user.email }, "secret");

  return c.json(
    {
      message: "Login successful",
      token,
    },
    200
  );
});

router.get("/profile", jwt({ secret: process.env.JWT_SECRET! }), async (c) => {

  const payload = c.get("jwtPayload");

  const user = {
    ...users.find((u) => u.email === payload.email),
    password: undefined
  }

  return c.json(
    {
      message: "Profile",
      data: user
    },
    200
  );
});
