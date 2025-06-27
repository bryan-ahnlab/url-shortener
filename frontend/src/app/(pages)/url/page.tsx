// src/app/shorten/page.tsx

import ShortenUrlForm from "@/components/ShortenUrlForm";

export default function ShortenPage() {
  return (
    <div className="w-[360px] mx-auto px-5 py-10">
      <ShortenUrlForm />
    </div>
  );
}
