"use client";

import { useState } from "react";
import { shortenUrl } from "@/actions/shorten";
import { ApiError } from "@/types/error";
import { ShortenUrlData } from "@/types/response";
import { normalizeUrl } from "@/utils/utility";

export default function ShortenUrlForm() {
  /* Request State */
  const [longUrl, setLongUrl] = useState<string | null>(null);
  const [description, setDescription] = useState<string | null>(null);

  /* Request Error State */
  const [inputLongUrlError, setInputLongUrlError] = useState<string | null>(
    null
  );

  /* Response State */
  const [data, setData] = useState<ShortenUrlData | null>(null);

  /* Response Error State */
  const [error, setError] = useState<ApiError | null>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (!longUrl?.trim()) {
      setInputLongUrlError("URL을 입력해주세요.");
      setData(null);
      return;
    } else {
      setInputLongUrlError(null);
    }

    const formData = new FormData(event.currentTarget);
    formData.append("long_url", longUrl);

    const apiResponse = await shortenUrl(formData);

    if (apiResponse.ok) {
      setData(apiResponse.data);
      setError(null);
    } else {
      setData(null);
      setError(apiResponse.error);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-4 p-6 border border-white/10 rounded-xl shadow-xl backdrop-blur-lg bg-white/5 w-full min-w-[360px]"
    >
      <h2 className="text-lg font-semibold text-white text-center">
        Enter URL
      </h2>

      {/* Long URL 입력 */}
      <div className="flex flex-col gap-2.5 w-full">
        <label className="text-sm text-white" htmlFor="long_url">
          Long URL:
        </label>
        <input
          className={`w-full bg-black/20 border ${
            inputLongUrlError ? "border-red-500" : "border-white/20"
          } rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10`}
          type="text"
          id="long_url"
          placeholder="https://example.com"
          value={longUrl || ""}
          onChange={(e) => setLongUrl(e.target.value)}
        />
        {/* Long URL 에러 메시지 */}
        {inputLongUrlError && (
          <p className="text-red-400 text-sm">{inputLongUrlError}</p>
        )}
      </div>

      {/* Description 입력 */}
      <div className="flex flex-col gap-2.5 w-full">
        <label className="text-sm text-white" htmlFor="description">
          Description (Optional):
        </label>
        <input
          className="w-full bg-black/20 border border-white/20 rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10"
          type="text"
          id="description"
          name="description"
          placeholder="설명을 입력하세요"
          value={description || ""}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>

      {/* 공백 */}
      <div className="h-4"></div>

      {/* 제출 버튼 */}
      <button
        type="submit"
        className="w-full bg-white border border-black/20 rounded px-3 py-2 text-black text-sm font-bold focus:ring-2 focus:ring-black focus:border-black/10 shadow-md cursor-pointer hover:bg-gray-200"
      >
        Shorten
      </button>

      {/* 결과 표시 */}
      {data && (
        <div className="mt-5 p-4 border border-white/10 rounded-xl bg-white/5 text-white text-sm space-y-1 break-all">
          <p>
            <strong>ID:&nbsp;</strong>
            {data.response.id}
          </p>
          <p>
            <strong>Description:&nbsp;</strong>
            {data.response.description || "-"}
          </p>
          <p>
            <strong>Long URL:&nbsp;</strong>
            <a
              href={normalizeUrl(data.response.long_url)}
              className="text-blue-400 hover:underline break-all"
              target="_blank"
              rel="noopener noreferrer"
            >
              {normalizeUrl(data.response.long_url)}
            </a>
          </p>
          <p>
            <strong>Short URL:&nbsp;</strong>
            <a
              href={`${process.env.NEXT_PUBLIC_BACKEND_URL}/${data.response.short_url}`}
              className="text-blue-400 hover:underline break-all"
              target="_blank"
              rel="noopener noreferrer"
            >
              {`${process.env.NEXT_PUBLIC_BACKEND_URL}/${data.response.short_url}`}
            </a>
          </p>
        </div>
      )}

      {/* 에러 표시 */}
      {error && (
        <div className="mt-5 p-4 border border-red-500 rounded-xl bg-red-500/10 text-red-400 text-sm space-y-1 break-all">
          <p>
            <strong>Title:&nbsp;</strong>
            {error.title}
          </p>
          <p>
            <strong>Detail:&nbsp;</strong>
            {error.detail}
          </p>
          <p>
            <strong>Status:&nbsp;</strong>
            {error.status}
          </p>
          <p>
            <strong>Type:&nbsp;</strong>
            <a
              href={error.type}
              target="_blank"
              className="underline text-blue-400 break-all"
            >
              {error.type}
            </a>
          </p>
          <p>
            <strong>Method:&nbsp;</strong>
            {error.method}
          </p>
          <p>
            <strong>Instance:&nbsp;</strong>
            <a
              href={error.instance}
              target="_blank"
              className="underline text-blue-400 break-all"
            >
              {error.instance}
            </a>
          </p>
        </div>
      )}
    </form>
  );
}
