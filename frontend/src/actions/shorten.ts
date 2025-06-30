"use server";

import { ApiError, DEFAULT_API_ERROR } from "@/types/error";
import { safeParseJson } from "@/utils/utility";

export async function shortenUrl(formData: FormData) {
  const formObject = Object.fromEntries(formData.entries());

  try {
    const response = await fetch(`${process.env.BASE_URL}/api/url`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formObject),
    });

    const contentType = response.headers.get("content-type");

    let data = null;

    if (contentType?.includes("application/json")) {
      data = await safeParseJson(response);
    } else {
      const text = await response.text();
      data = { detail: text || "Unexpected non-JSON response" };
    }

    if (!response.ok) {
      const error = new ApiError({
        type: data?.type || "",
        title: data?.title || "Error",
        status: response.status,
        detail: data?.detail || "Unexpected error",
        instance: data?.instance || "",
        method: data?.method || "",
      });

      return {
        ok: false,
        error: error.toJSON(),
      };
    }

    return {
      ok: true,
      data,
    };
  } catch (error) {
    console.error("서버 연결 실패 또는 기타 오류:", error);

    return {
      ok: false,
      error: DEFAULT_API_ERROR,
    };
  }
}
