import { create } from "zustand";
import { persist } from "zustand/middleware";

type Store = {
  users: any;
  edit?: boolean;
};

const initialState: Store = {
  users: [],
  edit: false,
};

type Actions = {
  addUser: (users: any) => void;
  setUsers: (users: []) => void;
  setEdit: (isEdit: boolean) => void;
  reset: () => void;
};

type StoreWithActions = Store & Actions;

export const userStore = create(
  persist<StoreWithActions>(
    (set) => ({
      ...initialState,
      addUser: (users) =>
        set((state) => {
          if (users) {
            return { users: [...state.users, users] };
          }
          return state;
        }),
      setUsers: (users) =>
        set(() => {
          return {
            users,
          };
        }),
      setEdit: (isEdit: boolean) =>
        set(() => {
          return {
            edit: isEdit,
          };
        }),
      reset: () => set(initialState),
    }),
    { name: "users" }
  )
);
