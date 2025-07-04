// src/app/shorten/page.tsx

import CreateShortUrlForm from "@/components/CreateShortUrlForm";

export default function ShortUrlPage() {
  return (
    <div className="mx-auto px-5 py-10">
      <CreateShortUrlForm />
    </div>
  );
}
