import { NextRequest, NextResponse } from "next/server";

const backendBaseUrl =
  process.env.BACKEND_API_URL ?? "http://localhost:8000";

export async function POST(request: NextRequest) {
  try {
    const payload = await request.json();

    const upstream = await fetch(`${backendBaseUrl}/api/v1/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      cache: "no-store",
    });

    if (!upstream.ok) {
      return NextResponse.json(
        { error: "Backend request failed." },
        { status: upstream.status },
      );
    }

    const data = await upstream.json();
    return NextResponse.json(data);
  } catch {
    return NextResponse.json(
      { error: "Could not reach backend service." },
      { status: 500 },
    );
  }
}
