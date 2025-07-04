export default function ShortenLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex flex-col h-screen justify-center items-center bg-black text-white relative overflow-hidden">
      {/* 신호등 조명 */}
      <div className="absolute top-24 left-24 w-72 h-72 bg-red-700 opacity-25 rounded-full blur-2xl z-0 animate-ping"></div>
      <div className="absolute top-40 right-20 w-48 h-48 bg-yellow-500 opacity-20 rounded-full blur-2xl z-0 animate-pulse"></div>
      <div className="absolute bottom-32 left-36 w-64 h-64 bg-green-500 opacity-20 rounded-full blur-2xl z-0 animate-ping"></div>

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

      {/* 콘텐츠 */}
      <div className="z-10">{children}</div>

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
