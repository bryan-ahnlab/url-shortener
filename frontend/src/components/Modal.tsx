"use client";

import { useAppDispatch, useAppSelector } from "@/store/hooks";
import { closeModal } from "@/store/modalSlice";

export default function Modal() {
  const dispatch = useAppDispatch();
  const { isOpen, title, contents } = useAppSelector((state) => state.modal);

  if (!isOpen) return null;

  return (
    <div
      className="fixed inset-0 flex items-center justify-center bg-black/70 z-50"
      onClick={() => dispatch(closeModal())}
    >
      <div
        className="bg-white p-6 rounded-lg shadow-xl text-black w-80 text-center min-w-[360px]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* 제목 */}
        <h2 className="text-lg font-semibold mb-4">{title}</h2>

        {/* 내용 배열 */}
        <div className="text-sm text-left mb-4 space-y-2 break-all">
          {contents?.map((line, idx) => (
            <p key={idx}>• {line}</p>
          ))}
        </div>

        {/* 닫기 버튼 */}
        <button
          onClick={() => dispatch(closeModal())}
          className="w-full bg-white border border-black/20 rounded px-3 py-2 text-black text-sm font-bold focus:ring-2 focus:ring-black focus:border-black/10 shadow-md cursor-pointer hover:bg-gray-200 text-center flex items-center justify-center"
        >
          닫기
        </button>
      </div>
    </div>
  );
}
