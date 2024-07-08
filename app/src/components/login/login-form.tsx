import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { loginService } from "@/services/service";
import { useAuthStore } from "@/store/authStore";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { useToast } from "../ui/use-toast";
export const LoginForm = () => {
  const navigate = useNavigate();
  const { toast } = useToast();
  const formSchema = z.object({
    email: z.string().min(2).max(30),
    password: z.string().min(2).max(30),
  });

  const formLogin = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
      password: "",
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      const data = await loginService(values);
      useAuthStore.getState().setToken(data.access_token, data.user_info);
      toast({
        title: "Login success",
        className: "bg-slate-900 text-white",
        duration: 1000,
      });
      formLogin.reset();
      debugger;
      if (data.user_info.type === "user" && data.user_info.is_superuser) {
        navigate("/user");
      } else {
        navigate("/vehicle");
      }
    } catch (error) {
      toast({
        title: "Login error user not found",
        className: "bg-red-500 text-white",
        duration: 1000,
      });
      navigate("/user");
    }
  }
  return (
    <div>
      <Form {...formLogin}>
        <form onSubmit={formLogin.handleSubmit(onSubmit)} className="space-y-2">
          <FormField
            control={formLogin.control}
            name="email"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Username</FormLabel>
                <FormControl>
                  <Input placeholder="usr.daniel" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <FormField
            control={formLogin.control}
            name="password"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Password</FormLabel>
                <FormControl>
                  <Input type="password" placeholder="*******" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
          <div className="flex items-center justify-between">
            <Button type="submit">Login</Button>
            <NavLink to="/report">
              <span className="text-sm font-bold hover:underline">
                View report
              </span>
            </NavLink>
          </div>
        </form>
      </Form>
    </div>
  );
};
