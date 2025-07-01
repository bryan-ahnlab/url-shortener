// /actions/short-url.ts
"use server";

import { ApiResult, ShortenUrlData } from "@/types/response";
import { safeParseJson } from "@/utils/utility";

export async function createShortUrl(
  formData: FormData
): Promise<ApiResult<ShortenUrlData>> {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/short-url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  const data = await safeParseJson(response);

  console.log(`createShortUrl`, data);

  return data;
}
