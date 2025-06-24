import Link from "next/link";

export default function NotFound() {
  return (
    <div className="relative flex flex-col h-screen justify-center items-center text-center bg-black text-white overflow-hidden">
      {/* 신호등 조명 - 다양한 위치와 크기 */}
      <div className="absolute top-24 left-24 w-72 h-72 bg-red-600 opacity-20 rounded-full blur-2xl z-0 animate-ping"></div>
      <div className="absolute top-40 right-20 w-48 h-48 bg-green-500 opacity-20 rounded-full blur-2xl z-0 animate-pulse"></div>
      <div className="absolute bottom-32 left-36 w-64 h-64 bg-yellow-400 opacity-20 rounded-full blur-2xl z-0 animate-ping"></div>
      <div className="absolute top-1/4 left-1/3 w-52 h-52 bg-red-500 opacity-15 rounded-full blur-2xl z-0 animate-pulse"></div>
      <div className="absolute bottom-20 right-1/4 w-40 h-40 bg-green-400 opacity-15 rounded-full blur-2xl z-0 animate-ping"></div>
      <div className="absolute bottom-36 left-1/5 w-56 h-56 bg-yellow-300 opacity-15 rounded-full blur-2xl z-0 animate-pulse"></div>

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
      <div className="z-10 flex flex-col items-center p-6 sm:p-10 rounded-xl border border-white/10 backdrop-blur-md bg-white/5 shadow-xl w-11/12 max-w-2xl">
        <h1 className="text-5xl sm:text-7xl font-extrabold mb-4 text-white drop-shadow-lg">
          404
        </h1>
        <p className="text-lg sm:text-xl text-gray-300 mb-6 w-full text-center">
          Sorry, the page you are looking for could not be found.
        </p>
        <Link
          href="/"
          className="px-6 py-3 bg-white text-black font-bold rounded-lg shadow-lg hover:scale-105 transition-transform duration-300 hover:bg-gray-200"
        >
          ⬅ Return to Home
        </Link>
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
