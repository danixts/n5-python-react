import { getAllUsers } from "@/services/service";
import { TableUser } from "./table-user";
import { FormUser } from "./form-user";
import { userStore } from "@/store/userStore";

export default function UserPage() {
  const { users, setUsers } = userStore();
  useEffect(() => {
    const exec = async () => {
      const data = await getAllUsers();
      setUsers(data);
    };
    exec();
  }, []);
  return (
    <>
      <div className="flex items-center space-x-4">
        <h1 className="text-lg font-semibold md:text-2xl">Users</h1>
        <FormUser />
      </div>
      <div className="flex flex-1 rounded-lg border border-dashed shadow-sm p-5">
        <TableUser data={users} />
      </div>
    </>
  );
}
