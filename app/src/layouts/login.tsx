import { App } from "@/page/login";
import { Toaster } from "@/components/ui/toaster";
export const LoginLayout = () => {
  return (
    <>
      <div className="container mx-auto flex justify-center mt-28">
        <App />
      </div>
      <Toaster />
    </>
  );
};
