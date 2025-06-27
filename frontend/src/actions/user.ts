"use server";

async function safeParseJson(response: Response) {
  try {
    return await response.json();
  } catch {
    return null;
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function handleResponse(response: Response, data: any) {
  if (!response.ok) {
    return (
      data || {
        status: response.status,
        title: "Error",
        detail: response.statusText || "Unexpected error",
      }
    );
  }
  return data;
}

export async function signUpUser(formData: FormData) {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/user/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  const data = await safeParseJson(response);
  return handleResponse(response, data);
}

export async function loginUser(formData: FormData) {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(`${process.env.BASE_URL}/api/user/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formObject),
  });

  const data = await safeParseJson(response);
  return handleResponse(response, data);
}

export async function updateUser(email: string, formData: FormData) {
  const formObject = Object.fromEntries(formData.entries());

  const response = await fetch(
    `${process.env.BASE_URL}/api/user/update/${email}`,
    {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formObject),
    }
  );

  const data = await safeParseJson(response);
  return handleResponse(response, data);
}

export async function deleteUser(email: string) {
  const response = await fetch(
    `${process.env.BASE_URL}/api/user/delete/${email}`,
    {
      method: "DELETE",
    }
  );

  const data = await safeParseJson(response);
  return handleResponse(response, data);
}
