"use client";

import { useState } from "react";
import { loginUser } from "@/actions/user";

export default function UserLoginForm() {
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);
    const response = await loginUser(formData);

    if (response.status === 200) {
      setMessage(`Welcome, ${response.name}!`);
    } else {
      setMessage(response.detail || "Login failed");
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col gap-4 p-6 border border-white/10 rounded-xl shadow-xl backdrop-blur-lg bg-white/5 w-full max-w-md"
    >
      <h2 className="text-lg font-semibold text-white text-center">Login</h2>

      <input
        className="bg-black/20 border border-white/20 rounded px-3 py-2 text-white placeholder-gray-400"
        type="email"
        name="email"
        placeholder="Email"
        required
      />

      <input
        className="bg-black/20 border border-white/20 rounded px-3 py-2 text-white placeholder-gray-400"
        type="password"
        name="password"
        placeholder="Password"
        required
      />

      <button
        type="submit"
        className="bg-yellow-400 text-black font-bold py-2 px-4 rounded hover:scale-105 transition-transform duration-300"
      >
        Login
      </button>

      {message && (
        <div className="mt-4 text-sm text-white text-center">{message}</div>
      )}
    </form>
  );
}
