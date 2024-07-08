import { getAllInfractions } from "@/services/service";
import { TableInfraction } from "./table-infraction";
import { useAuthStore } from "@/store/authStore";

export default function InfractionPage() {
  const [infractions, setInfractions] = useState([]);
  const { userInfo } = useAuthStore();
  useEffect(() => {
    const exec = async () => {
      const data = await getAllInfractions(userInfo?.email);
      setInfractions(data);
    };
    exec();
  }, []);
  return (
    <>
      <div className="flex items-center space-x-4">
        <h1 className="text-lg font-semibold md:text-2xl">Infractions</h1>
      </div>
      <div className="flex flex-1 rounded-lg border border-dashed shadow-sm p-5">
        <TableInfraction data={infractions} />
      </div>
    </>
  );
}
