import { decode, sign, verify } from "hono/jwt";
import { env } from "../config/env";
import { Context, Next } from "hono";

export const auth = async (c: Context, next: Next) => {};
