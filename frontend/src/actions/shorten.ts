"use server";

export async function shortenUrl(formData: FormData) {
  const formObject = Object.fromEntries(formData.entries());

  try {
    const response = await fetch(`${process.env.BASE_URL}/api/url`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formObject),
    });

    const data = await response.json();

    return data;
  } catch (error) {
    console.error("Server Action Error:", error);
    throw error;
  }
}
