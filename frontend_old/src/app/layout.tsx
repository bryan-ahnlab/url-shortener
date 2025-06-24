import Link from "next/link";

export default function NotFound() {
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
      <div className="z-10 flex flex-col items-center px-4 sm:px-6 md:px-8 py-6 sm:py-8 md:py-10 rounded-xl border border-white/10 backdrop-blur-md bg-white/5 shadow-xl w-11/12 max-w-5xl">
        {/* 제목 */}
        <h1 className="text-4xl sm:text-6xl md:text-7xl lg:text-8xl font-extrabold mb-6 text-white drop-shadow-xl tracking-wide text-center break-words">
          404 - Page Not Found
        </h1>

        {/* 설명 */}
        <p className="text-base sm:text-lg md:text-xl lg:text-2xl text-gray-300 mb-8 w-full text-center leading-relaxed max-w-4xl flex flex-wrap justify-center break-words">
          <span className="font-semibold text-white">
            Sorry, the page you&apos;re looking for does not exist.
          </span>
          <span className="ml-2">
            Please check the URL or return to the homepage.
          </span>
        </p>

        {/* 버튼 */}
        <div className="flex gap-6 flex-wrap justify-center">
          <Link
            href="/"
            className="px-5 py-3 bg-white text-black font-bold rounded-lg shadow-lg hover:scale-105 transition-transform duration-300 hover:bg-gray-200"
          >
            Home
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
