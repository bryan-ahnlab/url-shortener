import { configureStore } from "@reduxjs/toolkit";
import modalReducer from "@/store/modalSlice";
import loadingReducer from "@/store/loadingSlice";

export const store = configureStore({
  reducer: {
    modal: modalReducer,
    loading: loadingReducer,
  },
});

// 타입 선언
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
