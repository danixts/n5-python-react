import { useAuthStore } from "@/store/authStore";
import { FC, ReactNode } from "react";
import { Navigate } from "react-router-dom";

const ProtectedRoutes: FC<{ children: ReactNode }> = ({ children }) => {
  const isAuthenticated = useAuthStore((state) => state.isAuth);
  const location = useLocation();
  if (location.pathname === "/" && !isAuthenticated ) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }
  return children;
};

export default ProtectedRoutes;
