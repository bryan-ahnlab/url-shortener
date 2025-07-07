"use client";

import { useAppSelector } from "@/store/hooks";

export default function Loading() {
  const isLoading = useAppSelector((state) => state.loading.isLoading);

  if (!isLoading) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center bg-black/70 z-50">
      <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-white border-opacity-50"></div>
    </div>
  );
}
