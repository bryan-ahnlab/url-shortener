import { NextRequest, NextResponse } from "next/server";

export async function POST(rawRequest: NextRequest) {
  const request = await rawRequest.json();

  const response = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(request),
  });

  console.log(`response`, response);

  const data = await response.json();

  return NextResponse.json(data);
}
