import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const body = await req.json();

  const apiRes = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/url`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  const apiBody = await apiRes.json();
  console.log(`apiRes`, apiRes);

  if (apiRes.ok) {
    return NextResponse.json({ shortUrl: apiBody.data.item.short_url });
  } else {
    return NextResponse.json({ detail: apiBody.detail }, { status: 400 });
  }
}
