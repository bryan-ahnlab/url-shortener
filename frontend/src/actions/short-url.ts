"use server";

import { ApiError, DEFAULT_API_ERROR } from "@/types/error";
import { safeParseJson } from "@/utils/utility";
import { ApiResult, ShortenUrlData } from "@/types/response";

export async function createShortUrl(
  formData: FormData
): Promise<ApiResult<ShortenUrlData>> {
  const formObject = Object.fromEntries(formData.entries());

  try {
    const apiResponse = await fetch(`${process.env.BASE_URL}/api/short-url`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formObject),
    });

    const contentType = apiResponse.headers.get("content-type");
    const responseData = contentType?.includes("application/json")
      ? await safeParseJson(apiResponse)
      : {
          detail: (await apiResponse.text()) || "Unexpected non-JSON response",
        };

    if (!apiResponse.ok) {
      return {
        ok: false,
        error: new ApiError({
          type: responseData?.type || "",
          title: responseData?.title || "Error",
          status: apiResponse.status,
          detail: responseData?.detail || "Unexpected error",
          instance: responseData?.instance || "",
          method: responseData?.method || "POST",
        }),
      };
    }

    return {
      ok: true,
      data: responseData,
    };
  } catch (error) {
    console.error("Error:", error);
    return {
      ok: false,
      error: new ApiError(DEFAULT_API_ERROR),
    };
  }
}
