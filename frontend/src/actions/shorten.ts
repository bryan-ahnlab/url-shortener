"use server";

import { ApiError, DEFAULT_API_ERROR } from "@/types/error";
import { safeParseJson } from "@/utils/utility";
import { ApiResult, ShortenUrlData } from "@/types/response";

export async function shortenUrl(
  formData: FormData
): Promise<ApiResult<ShortenUrlData>> {
  const formObject = Object.fromEntries(formData.entries());

  try {
    const apiResponse = await fetch(`${process.env.BASE_URL}/api/url`, {
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

    const mappedData = {
      status: responseData.status,
      message: responseData.message,
      request: responseData.request,
      response: responseData.data,
    };

    return {
      ok: true,
      data: mappedData,
    };
  } catch (error) {
    console.error("Error:", error);
    return {
      ok: false,
      error: new ApiError(DEFAULT_API_ERROR),
    };
  }
}
