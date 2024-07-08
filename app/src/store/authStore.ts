import { create } from "zustand";
import { persist } from "zustand/middleware";

export interface UserInfo {
  id?: number;
  username?: string;
  email?: string;
  is_superuser?: boolean;
  type?: string;
  is_active?: boolean;
}

type Store = {
  token: string;
  userId: string;
  isAuth: boolean;
  userInfo?: UserInfo;
};

type Actions = {
  setToken: (token: string, userInfo: UserInfo) => void;
  reset: () => void;
};

const initialState: Store = {
  token: "",
  userId: "",
  isAuth: false,
  userInfo: {},
};

export const useAuthStore = create(
  persist<Store & Actions>(
    (set) => ({
      ...initialState,
      reset: () => set(initialState),
      setToken: (token, userInfo) =>
        set(() => {
          const isAuth = !!token;
          return {
            token,
            userId: "1",
            isAuth,
            userInfo,
          };
        }),
    }),
    { name: "auth" }
  )
);
