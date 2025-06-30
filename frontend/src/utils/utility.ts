export async function safeParseJson(response: Response) {
  try {
    return await response.json();
  } catch {
    return null;
  }
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function handleResponse(response: Response, data: any) {
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
