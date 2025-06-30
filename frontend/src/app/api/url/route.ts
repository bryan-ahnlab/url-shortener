import { NextRequest, NextResponse } from "next/server";

export async function POST(rawRequest: NextRequest) {
  const body = await rawRequest.json();

  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/url`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const contentType = response.headers.get("content-type");
    const isJson = contentType?.includes("application/json");

    const data = isJson
      ? await response.json()
      : { detail: (await response.text()) || "Unexpected non-JSON response" };

    return NextResponse.json(data, { status: response.status });
  } catch (error) {
    return NextResponse.json(
      { detail: String(error), status: 500 },
      { status: 500 }
    );
  }
}
