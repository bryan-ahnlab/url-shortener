"use client";

import { createContext, useContext, useState, ReactNode } from "react";
import { LoginUserData } from "@/types/response";

interface UserContextType {
  user: LoginUserData["response"] | null;
  setUser: (user: LoginUserData["response"] | null) => void;
}

const UserContext = createContext<UserContextType | null>(null);

export function UserProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<LoginUserData["response"] | null>(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  const context = useContext(UserContext);
  if (!context) throw new Error("useUser must be used within UserProvider");
  return context;
}
