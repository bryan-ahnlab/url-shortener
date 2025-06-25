"use client";

import { useState } from "react";
import { shortenUrl } from "@/actions/shorten";

export default function ShortenUrlForm() {
  const [shortUrl, setShortUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const result = await shortenUrl(formData);
    console.log(`result`, result);
    console.log(`result`, result.ok);

    if (result.status === 200) {
      setShortUrl(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/${result.data.short_url}`
      );
      setError(null);
    } else {
      setError(result.detail || "An error occurred");
      setShortUrl(null);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-4 p-6 border border-white/10 rounded-xl shadow-xl backdrop-blur-lg bg-white/5 w-full max-w-md"
    >
      <h2 className="text-lg font-semibold text-white text-center">
        Enter URL to Shorten
      </h2>

      <div className="flex flex-col gap-2.5">
        <label className="text-sm text-white" htmlFor="long_url">
          Original URL:
        </label>
        <input
          className="bg-black/20 border border-white/20 rounded px-3 py-2 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-yellow-400 focus:border-yellow-400 text-sm"
          type="text"
          name="long_url"
          id="long_url"
          placeholder="https://example.com"
          required
        />
      </div>

      <button
        type="submit"
        className="bg-yellow-400 text-black font-bold py-2 px-4 rounded hover:scale-105 transition-transform duration-300 hover:bg-yellow-300 text-sm shadow-md"
      >
        Shorten URL
      </button>

      {shortUrl && (
        <div className="mt-5 p-4 border border-white/10 rounded-xl backdrop-blur-md bg-white/5 text-sm text-white">
          <p className="mb-1">Shortened URL:</p>
          <a
            href={shortUrl}
            className="text-blue-400 hover:underline break-words"
            target="_blank"
            rel="noopener noreferrer"
          >
            {shortUrl}
          </a>
        </div>
      )}

      {error && (
        <div className="mt-5 p-4 border border-red-500 rounded-xl bg-red-500/10 text-red-400 text-sm">
          <p>{error}</p>
        </div>
      )}
    </form>
  );
}
