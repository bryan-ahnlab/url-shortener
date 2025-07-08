"use client";
import { createContext, useContext, useState, ReactNode } from "react";

interface ModalFunction {
  label: string;
  onClick: () => void;
}

interface ModalContextType {
  isOpen: boolean;
  title: string | null;
  contents: string[] | null;
  functions: ModalFunction[] | null;
  openModal: (args: {
    title: string;
    contents: string[];
    functions: ModalFunction[];
  }) => void;
  closeModal: () => void;
}

const ModalContext = createContext<ModalContextType | null>(null);

export const ModalProvider = ({ children }: { children: ReactNode }) => {
  const [isOpen, setIsOpen] = useState(false);

  const [title, setTitle] = useState<string | null>(null);
  const [contents, setContents] = useState<string[] | null>(null);
  const [functions, setFunctions] = useState<ModalFunction[] | null>(null);

  const openModal = ({
    title,
    contents,
    functions,
  }: {
    title: string;
    contents: string[];
    functions: ModalFunction[];
  }) => {
    setIsOpen(true);
    setTitle(title);
    setContents(contents);
    setFunctions(functions);
  };

  const closeModal = () => {
    setIsOpen(false);
    setTitle(null);
    setContents(null);
    setFunctions(null);
  };

  return (
    <ModalContext.Provider
      value={{ isOpen, title, contents, functions, openModal, closeModal }}
    >
      {children}
    </ModalContext.Provider>
  );
};

export const useModal = (): ModalContextType => {
  const context = useContext(ModalContext);
  if (!context) throw new Error("useModal must be used within a ModalProvider");
  return context;
};
