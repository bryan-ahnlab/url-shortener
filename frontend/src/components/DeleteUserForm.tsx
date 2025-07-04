"use client";

import { useState } from "react";
import { deleteUser } from "@/actions/user";
import { ApiErrorShape } from "@/types/error";
import { DeleteUserData } from "@/types/response";
import { useRouter } from "next/navigation";
import { ArrowLeftIcon } from "@heroicons/react/24/solid";

export default function DeleteUserForm() {
  const [id, setId] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<ApiErrorShape | null>(null);
  const [data, setData] = useState<DeleteUserData | null>(null);

  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("id", id);
    formData.append("email", email);
    formData.append("password", password);

    const res = await deleteUser(formData);
    console.log(res);

    if (res.ok) {
      setData(res.data);
      setError(null);
    } else {
      setError(res.error);
      setData(null);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-4 p-6 border border-white/10 rounded-xl shadow-xl backdrop-blur-lg bg-white/5 w-full min-w-[360px]"
    >
      <div className="flex items-center gap-2">
        <button
          type="button"
          onClick={() => router.back()}
          className="text-white/80 hover:text-white cursor-pointer"
        >
          <ArrowLeftIcon className="w-5 h-5" />
        </button>
        <h2 className="text-lg font-semibold text-white">회원 탈퇴</h2>
      </div>

      <input
        className="w-full bg-black/20 border border-white/20 rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10"
        placeholder="회원 ID"
        value={id}
        onChange={(e) => setId(e.target.value)}
        required
      />
      <input
        className="w-full bg-black/20 border border-white/20 rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10"
        placeholder="이메일"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <input
        className="w-full bg-black/20 border border-white/20 rounded px-3 py-2 text-white text-sm placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white focus:border-white/10"
        placeholder="비밀번호"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
        type="password"
      />

      <button
        type="submit"
        className="w-full bg-red-500 border border-red-700 rounded px-3 py-2 text-white text-sm font-bold focus:ring-2 focus:ring-red-500 focus:border-red-700 shadow-md cursor-pointer hover:bg-red-600"
      >
        회원 탈퇴
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
