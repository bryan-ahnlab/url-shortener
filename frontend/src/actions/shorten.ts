"use server";

export async function shortenUrl(formData: FormData) {
  const formObject = Object.fromEntries(formData.entries());

  console.log(formData.entries());

  console.log(`formObject`, formObject);

  try {
    const response = await fetch(`${process.env.BASE_URL}/api/url`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formObject),
    });

    const body = await response.json();

    console.log(`response`, body);

    if (response.ok) {
      return {
        ok: true,
        shortUrl: `${process.env.NEXT_PUBLIC_BACKEND_URL}/${body.shortUrl}`,
      };
    } else {
      return { ok: false, error: body.detail || "An error occurred" };
    }
  } catch (error) {
    console.error("Server Action Error:", error);
    return { ok: false, error: "An error occurred" };
  }
}
