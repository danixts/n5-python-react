import { Button } from "@/components/ui/button";

export const LayoutError = () => {
  return (
    <div className="bg-slate-950 text-white">
      <div className="container flex justify-center items-center h-lvh w-full ">
      <div className="flex flex-col items-center space-y-6">
        <h1 className="text-3xl font-bold">Error Page 404</h1>
        <h1 className="text-lg text-center">Not Found</h1>
        <NavLink to="/login">
          <Button className="bg-green-500 text-xl font-bold py-8 px-16 shadow-lg shadow-green-500/50 hover:bg-green-400">Ir A Inicio</Button>
        </NavLink>
      </div>
    </div>
    </div>
  );
};
