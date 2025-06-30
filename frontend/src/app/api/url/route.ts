import { NextRequest, NextResponse } from "next/server";

export async function POST(rawRequest: NextRequest) {
  const body = await rawRequest.json();

  try {
    const apiResponse = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/url`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      }
    );

    const contentType = apiResponse.headers.get("content-type");
    const isJson = contentType?.includes("application/json");

    const response = isJson
      ? await apiResponse.json()
      : {
          detail: (await apiResponse.text()) || "Unexpected non-JSON response",
        };

    return NextResponse.json(response, { status: apiResponse.status });
  } catch (error) {
    return NextResponse.json(
      { detail: String(error), status: 500 },
      { status: 500 }
    );
  }
}
