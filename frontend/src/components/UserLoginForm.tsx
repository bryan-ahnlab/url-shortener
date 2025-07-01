"use client";

import { useState } from "react";
import { loginUser } from "@/actions/user";

export default function UserLoginForm() {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const [inputError, setInputError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    if (!email.trim() || !password.trim()) {
      setInputError("이메일과 비밀번호를 모두 입력해주세요.");
      setMessage(null);
      return;
    }

    setInputError(null);

    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    const response = await loginUser(formData);
    console.log(response);

    if (response.status === 200) {
      setMessage(`Welcome, ${response.name}!`);
    } else {
      setMessage(response.detail || "로그인에 실패했습니다.");
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
            inputError ? "border-red-500" : "border-white/20"
          } rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10`}
          type="email"
          id="email"
          placeholder="이메일을 입력하세요"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>

      {/* Password 입력 */}
      <div className="flex flex-col gap-2.5 w-full">
        <label className="text-sm text-white" htmlFor="password">
          Password:
        </label>
        <input
          className={`w-full bg-black/20 border ${
            inputError ? "border-red-500" : "border-white/20"
          } rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10`}
          type="password"
          id="password"
          placeholder="비밀번호를 입력하세요"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>

      {/* 공백 */}
      <div className="h-4"></div>

      {/* 오류 메시지 */}
      {inputError && <p className="text-red-400 text-sm">{inputError}</p>}

      {/* 로그인 버튼 */}
      <button
        type="submit"
        className="w-full bg-white border border-black/20 rounded px-3 py-2 text-black text-sm font-bold focus:ring-2 focus:ring-black focus:border-black/10 shadow-md cursor-pointer hover:bg-gray-200"
      >
        Login
      </button>

      {/* 결과 메시지 */}
      {message && (
        <div className="mt-4 text-sm text-white text-center">{message}</div>
      )}
    </form>
  );
}
