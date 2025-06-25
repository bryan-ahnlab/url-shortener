// src/app/shorten/page.tsx

import ShortenUrlForm from "@/components/ShortenUrlForm";

export default function ShortenPage() {
  return (
    <div className="w-[360px] mx-auto px-5 py-10">
      <h1 className="text-4xl font-bold mb-6 text-center">URL Shortener</h1>
      <ShortenUrlForm />
    </div>
  );
}
