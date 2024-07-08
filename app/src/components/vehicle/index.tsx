import { getVehicles } from "@/services/service";
import { FormVehicle } from "./form-vehicle";
import { vehicleStore } from "@/store/vehicleStore";
import { Card } from "../ui/card";
import { Badge } from "../ui/badge";
import { Search } from "lucide-react";
import { Input } from "../ui/input";
import { SetStateAction } from "react";
import { FormRegisterInfraction } from "./register-infraction";

interface Vehicle {
  id: number;
  model: string;
  color: string;
  car_plate: string;
}
export default function VehiclePage() {
  const { vehicles, setVehicles } = vehicleStore();
  const [searchTerm, setSearchTerm] = useState("");
  const [open, setOpen] = useState(false);
  const [selectVehicle, setSelectVehicle] = useState({});
  useEffect(() => {
    const exec = async () => {
      const data = await getVehicles();
      setVehicles(data);
    };
    exec();
  }, []);
  const handleOpenVehicle = (vehicle: any) => {
    setSelectVehicle(vehicle);
    setOpen(true);
  };
  const handleSearchChange = (event: {
    target: { value: SetStateAction<string> };
  }) => {
    setSearchTerm(event.target.value);
  };

  const filteredItems = vehicles
    ? vehicles.filter((vehicle: Vehicle) =>
        vehicle.car_plate.toLowerCase().includes(searchTerm.toLowerCase())
      )
    : [];
  return (
    <>
      <div className="flex flex-col items-start md:flex-row">
        <div className="flex items-center space-x-4">
          <h1 className="text-lg font-semibold md:text-2xl">Vehicle</h1>
          <FormVehicle />
        </div>
        <form className="mt-4 md:ml-auto w-full md:w-auto flex-1 md:mt-0 md:flex-initial">
          <div className="relative">
            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input
              onChange={handleSearchChange}
              type="search"
              placeholder="Search vehicle with plate..."
              className="pl-8 sm:w-[300px] md:w-[200px] lg:w-[300px]"
            />
          </div>
        </form>
      </div>
      {filteredItems.length > 0 && (
        <div className="flex p-4 rounded-lg border border-dashed shadow-sm">
          <div className="grid grid-cols-1 md:grid-cols-4 lg:grid-cols-4 gap-6 w-full">
            {filteredItems.map((vehicle: Vehicle) => {
              return (
                <Card
                  onClick={() => handleOpenVehicle(vehicle)}
                  key={vehicle.id}
                  className="p-5 space-y-2 hover:bg-slate-100 transition-colors duration-300 cursor-pointer"
                >
                  <h4 className="text-xl xl:text-2xl font-bold text-center">
                    {vehicle.car_plate}
                  </h4>
                  <p className="text-sm">{vehicle.model}</p>
                  <Badge className="items-start bg-gradient-to-tr from-slate-700 to-slate-900 border-none text-amber-50">
                    {vehicle.color}
                  </Badge>
                </Card>
              );
            })}
          </div>
        </div>
      )}
      {filteredItems.length === 0 && (
        <div
          className="flex flex-1 items-center justify-center rounded-lg border border-dashed shadow-sm"
          x-chunk="dashboard-02-chunk-1"
        >
          <div className="flex flex-col items-center gap-1 text-center">
            <h3 className="text-2xl font-bold tracking-tight">
              Not Vehicles register
            </h3>
            <p className="text-sm text-muted-foreground">not found</p>
          </div>
        </div>
      )}
      <FormRegisterInfraction
        open={open}
        setOpen={setOpen}
        vehicle={selectVehicle}
      />
    </>
  );
}
