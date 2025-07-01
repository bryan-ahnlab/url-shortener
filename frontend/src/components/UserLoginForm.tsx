"use client";

import { useState } from "react";
import { loginUser } from "@/actions/user";
import { ApiError } from "@/types/error";
import { LoginUserData } from "@/types/response";

export default function UserLoginForm() {
  /* Request State */
  const [email, setEmail] = useState<string | null>(null);
  const [password, setPassword] = useState<string | null>(null);

  /* Request Error State */
  const [inputEmailError, setInputEmailError] = useState<string | null>(null);
  const [inputPasswordError, setInputPasswordError] = useState<string | null>(
    null
  );

  /* Response State */
  const [data, setData] = useState<LoginUserData | null>(null);

  /* Response Error State */
  const [error, setError] = useState<ApiError | null>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (!email?.trim()) {
      setInputEmailError("이메일을 입력해주세요.");
      setData(null);
      return;
    } else {
      setInputEmailError(null);
    }

    if (!password?.trim()) {
      setInputPasswordError("비밀번호를 입력해주세요.");
      setData(null);
      return;
    } else {
      setInputPasswordError(null);
    }

    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    const apiResponse = await loginUser(formData);
    console.log(apiResponse);

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
      <h2 className="text-lg font-semibold text-white text-center">Login</h2>

      {/* Email 입력 */}
      <div className="flex flex-col gap-2.5 w-full">
        <label className="text-sm text-white" htmlFor="email">
          Email:
        </label>
        <input
          className={`w-full bg-black/20 border ${
            inputEmailError ? "border-red-500" : "border-white/20"
          } rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10`}
          type="email"
          id="email"
          placeholder="이메일을 입력하세요"
          value={email || ""}
          onChange={(e) => setEmail(e.target.value)}
        />
        {/* Email 에러 메시지 */}
        {inputEmailError && (
          <p className="text-red-400 text-sm">{inputEmailError}</p>
        )}
      </div>

      {/* Password 입력 */}
      <div className="flex flex-col gap-2.5 w-full">
        <label className="text-sm text-white" htmlFor="password">
          Password:
        </label>
        <input
          className={`w-full bg-black/20 border ${
            inputPasswordError ? "border-red-500" : "border-white/20"
          } rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10`}
          type="password"
          id="password"
          placeholder="비밀번호를 입력하세요"
          value={password || ""}
          onChange={(e) => setPassword(e.target.value)}
        />
        {/* Password 에러 메시지 */}
        {inputPasswordError && (
          <p className="text-red-400 text-sm">{inputPasswordError}</p>
        )}
      </div>

      {/* 공백 */}
      <div className="h-4"></div>

      {/* 로그인 버튼 */}
      <button
        type="submit"
        className="w-full bg-white border border-black/20 rounded px-3 py-2 text-black text-sm font-bold focus:ring-2 focus:ring-black focus:border-black/10 shadow-md cursor-pointer hover:bg-gray-200"
      >
        Login
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
