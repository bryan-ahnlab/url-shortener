"use client";

import { useState } from "react";
import { loginUser } from "@/actions/user";
import { ApiErrorShape } from "@/types/error";
import { LoginUserData } from "@/types/response";

import { EyeIcon, EyeSlashIcon } from "@heroicons/react/24/solid";

export default function CreateUserLoginForm() {
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
  const [error, setError] = useState<ApiErrorShape | null>(null);

  /* Password Visibility State */
  const [showPassword, setShowPassword] = useState(false);

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

        <div className="relative w-full">
          <input
            className={`w-full bg-black/20 border ${
              inputPasswordError ? "border-red-500" : "border-white/20"
            } rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10 pr-10`}
            type={showPassword ? "text" : "password"}
            id="password"
            placeholder="비밀번호를 입력하세요"
            value={password || ""}
            onChange={(e) => setPassword(e.target.value)}
          />

          {/* 아이콘 버튼 */}
          <button
            type="button"
            onClick={() => setShowPassword(!showPassword)}
            className="absolute inset-y-0 right-2 flex items-center text-white/60 hover:text-white cursor-pointer"
          >
            {showPassword ? (
              <EyeSlashIcon className="w-5 h-5" />
            ) : (
              <EyeIcon className="w-5 h-5" />
            )}
          </button>
        </div>

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
            <strong>Email:&nbsp;</strong>
            {data.response.email}
          </p>
          <p>
            <strong>Password:&nbsp;</strong>
            {data.response.password}
          </p>
          <p>
            <strong>Name:&nbsp;</strong>
            {data.response.name}
          </p>
          <p>
            <strong>Phone:&nbsp;</strong>
            {data.response.phone}
          </p>

          <p>
            <strong>Address:&nbsp;</strong>
            {data.response.address}
          </p>
          <p>
            <strong>Birth:&nbsp;</strong>
            {data.response.birth}
          </p>
          <p>
            <strong>Created At:&nbsp;</strong>
            {data.response.created_at}
          </p>
          <p>
            <strong>Updated At:&nbsp;</strong>
            {data.response.updated_at}
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
