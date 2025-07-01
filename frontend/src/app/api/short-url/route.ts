import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  try {
    const requestBody = await request.json();

    const apiResponse = await fetch(
      `${process.env.NEXT_PUBLIC_BACKEND_URL}/short-url`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody),
      }
    );

    const contentType = apiResponse.headers.get("content-type");
    const data = contentType?.includes("application/json")
      ? await apiResponse.json()
      : { detail: await apiResponse.text() };

    if (!apiResponse.ok) {
      return NextResponse.json(
        {
          ok: false,
          error: {
            type: data?.type || "",
            title: data?.title || "Error",
            status: apiResponse.status,
            detail: data?.detail || "Unexpected error",
            instance: data?.instance || "",
            method: "POST",
          },
        },
        { status: apiResponse.status }
      );
    }

    return NextResponse.json({ ok: true, data: data }, { status: 200 });
  } catch (error) {
    console.error(error);
    return NextResponse.json(
      {
        ok: false,
        error: {
          type: "about:blank",
          title: "Internal Server Error",
          status: 500,
          detail: String(error),
          instance: request.nextUrl.href,
          method: "POST",
        },
      },
      { status: 500 }
    );
  }
}
