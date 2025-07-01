"use client"; // Error boundaries must be Client Components

import { useEffect } from "react";
import Link from "next/link";

export default function Error({
  error,
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="relative flex flex-col h-screen justify-center items-center text-center bg-black text-white overflow-hidden">
      {/* 신호등 조명 */}
      <div className="absolute top-24 left-24 w-72 h-72 bg-red-700 opacity-25 rounded-full blur-2xl z-0 animate-ping"></div>
      <div className="absolute top-40 right-20 w-48 h-48 bg-yellow-500 opacity-20 rounded-full blur-2xl z-0 animate-pulse"></div>
      <div className="absolute bottom-32 left-36 w-64 h-64 bg-red-500 opacity-20 rounded-full blur-2xl z-0 animate-ping"></div>

      {/* 빗방울 효과 */}
      <div className="absolute inset-0 z-0 pointer-events-none rain-container">
        {Array.from({ length: 50 }).map((_, i) => (
          <span
            key={i}
            className="raindrop"
            style={{
              left: `${Math.random() * 100}%`,
              animationDuration: `${1 + Math.random() * 1.5}s`,
              animationDelay: `${Math.random() * 2}s`,
            }}
          />
        ))}
      </div>

      {/* 중앙 콘텐츠 */}
      <div className="z-10 flex flex-col items-center px-4 py-6 rounded-xl border border-white/10 backdrop-blur-md bg-white/5 shadow-xl max-w-5xl">
        {/* 제목 */}
        <h1 className="text-lg font-extrabold mb-6 text-white drop-shadow-xl tracking-wide text-center break-words">
          Oops!
        </h1>

        {/* 설명 */}
        <p className="text-lg text-gray-300 w-full text-center leading-relaxed max-w-4xl flex flex-wrap justify-center break-words flex-col mb-6">
          <span className="font-semibold text-white">
            An unexpected error occurred.
          </span>
          <span className="mx-2">
            Please try refreshing the page or return to the previous page.
          </span>
          <span className="mx-2">{error.message}</span>
        </p>

        {/* 버튼 */}
        <div className="w-full flex flex-row gap-4 justify-center">
          <button
            onClick={reset}
            className="w-full bg-white border border-black/20 rounded px-3 py-2 text-black text-sm font-bold focus:ring-2 focus:ring-black focus:border-black/10 shadow-md cursor-pointer hover:bg-gray-200"
          >
            Try Again
          </button>
          <Link
            href="/"
            className="w-full bg-white border border-black/20 rounded px-3 py-2 text-black text-sm font-bold focus:ring-2 focus:ring-black focus:border-black/10 shadow-md cursor-pointer hover:bg-gray-200"
          >
            Go Back
          </Link>
        </div>
      </div>

      {/* 스타일 정의 */}
      <style>{`
        .raindrop {
          position: absolute;
          top: -10px;
          width: 2px;
          height: 15px;
          background: rgba(255, 255, 255, 0.3);
          border-radius: 1px;
          animation: drop linear infinite;
        }

        @keyframes drop {
          to {
            transform: translateY(100vh);
          }
        }
      `}</style>
    </div>
  );
}
