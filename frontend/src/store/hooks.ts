import { TypedUseSelectorHook, useDispatch, useSelector } from "react-redux";
import type { RootState, AppDispatch } from "@/store";

// dispatch에 타입 적용
export const useAppDispatch = () => useDispatch<AppDispatch>();

// selector에 RootState 타입 적용
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
