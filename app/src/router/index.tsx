import { LayoutError } from "@/layouts/error";
import { LoginLayout } from "@/layouts/login";
import { LayoutDefault } from "@/layouts/normal";
import { createBrowserRouter } from "react-router-dom";
import ProtectedRoutes from "./protectRoute";
import UserPage from "@/components/user";
import VehiclePage from "@/components/vehicle";
import { ReportPage } from "@/components/report";
import InfractionPage from "@/components/infraction";

export const appRouter = createBrowserRouter(
  [
    {
      path: "/",
      element: (
        <ProtectedRoutes>
          <LayoutDefault />
        </ProtectedRoutes>
      ),
      children: [
        {
          path: "/user",
          element: <UserPage />,
        },
        {
          path: "/vehicle",
          element: <VehiclePage />,
        },
        {
          path: "/infraction",
          element: <InfractionPage />,
        },
      ],
    },
    {
      path: "/login",
      element: <LoginLayout />,
    },
    {
      path: "/report",
      element: <ReportPage />,
    },
    {
      path: "*",
      element: <LayoutError />,
    },
  ],
  {
    basename: "/",
  }
);
