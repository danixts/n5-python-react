import api from "@/services/api";
import { useAuthStore } from "@/store/authStore";
import { createContext, FC, ReactNode } from "react";

const AuthContext = createContext({});

export const useAuth = () => {
  const autContext = useContext(AuthContext);

  if (!autContext) {
    throw new Error("not context auth provider");
  }
  return autContext;
};

interface Auth {
  children: ReactNode;
}

export const AuthProvider: FC<Auth> = ({ children }) => {
  const [auth, setAuth] = useState({});

  useLayoutEffect(() => {
    const refresh = api.interceptors.response.use(
      (res) => res,
      (err) => {
        try {
          if (err.response.status === 403) {
            window.location.href = "/login";
            localStorage.removeItem("auth")
          }
        } catch (error) {
          useAuthStore.getState().reset()
          window.location.href = "/login";
          localStorage.removeItem("auth")
        }
        return Promise.reject(err);
      }
    );
    return () => {
      api.interceptors.response.eject(refresh);
    };
  }, []);

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};
