"use client";

import { useState } from "react";
import { shortenUrl } from "@/actions/shorten";

export default function ShortenUrlForm() {
  const [targetUrl, setTargetUrl] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const result = await shortenUrl(formData);

    if (result.ok) {
      setTargetUrl(result.shortUrl || "");
      setError("");
    } else {
      setError(result.error);
      setTargetUrl("");
    }
  };

  return (
    <div className="w-[360px] mx-auto px-5 py-10">
      <div className="flex flex-col gap-2.5">
        <div className="flex flex-col p-5">
          <span className="text-sm">URL Shortener</span>
        </div>
        <form
          onSubmit={handleSubmit}
          className="flex flex-col gap-4 p-5 border rounded shadow"
        >
          <div className="flex flex-col gap-2.5">
            <label className="text-sm" htmlFor="long_url">
              Original URL:
            </label>
            <input
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline text-sm"
              type="text"
              name="long_url"
              id="long_url"
              required
            />
          </div>
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline text-sm"
          >
            Shorten URL
          </button>
        </form>

        {targetUrl && (
          <div className="mt-5 p-5 border rounded shadow">
            <p className="text-sm">Shortened URL:</p>
            <a
              href={targetUrl}
              className="text-blue-500 hover:underline text-sm"
              target="_blank"
              rel="noopener noreferrer"
            >
              {targetUrl}
            </a>
          </div>
        )}
        {error && (
          <div className="mt-5 p-5 border rounded shadow text-red-500">
            <p>{error}</p>
          </div>
        )}
      </div>
    </div>
  );
}
