import { createSlice } from "@reduxjs/toolkit";

interface ModalState {
  isOpen: boolean;
  title: string | null;
  contents: string[] | null;
}

const initialState: ModalState = {
  isOpen: false,
  title: null,
  contents: null,
};

const modalSlice = createSlice({
  name: "modal",
  initialState,
  reducers: {
    openModal(state, action) {
      state.isOpen = true;
      state.title = action.payload.title;
      state.contents = action.payload.contents;
    },
    closeModal(state) {
      state.isOpen = false;
      state.title = null;
      state.contents = null;
    },
  },
});

export const { openModal, closeModal } = modalSlice.actions;
export default modalSlice.reducer;
