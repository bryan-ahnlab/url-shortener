import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { LoadingProvider } from "@/contexts/LoadingContext";
import { ModalProvider } from "@/contexts/ModalContext";
import Loading from "@/components/Loading";
import Modal from "@/components/Modal";

import { UserProvider } from "@/contexts/UserContext";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
  display: "swap",
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "App",
  description: "App by Next.js",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${geistSans.variable} ${geistMono.variable}`}>
      <body className="antialiased">
        <UserProvider>
          <LoadingProvider>
            <ModalProvider>
              {children}
              <Modal />
              <Loading />
            </ModalProvider>
          </LoadingProvider>
        </UserProvider>
      </body>
    </html>
  );
}
