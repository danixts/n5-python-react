import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "../ui/form";
import { createUser } from "@/services/service";
import { useToast } from "../ui/use-toast";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../ui/select";

import { Checkbox } from "../ui/checkbox";
import { userStore } from "@/store/userStore";

function getRandomInt() {
  const min = Math.ceil(100000);
  const max = Math.floor(1000000);
  return Math.floor(Math.random() * (max - min + 1)) + min; // El máximo es inclusivo y el mínimo es inclusivo
}

export const FormUser = () => {
  const [open, setOpen] = useState(false);
  const { toast } = useToast();
  const formSchema = z
    .object({
      username: z
        .string()
        .min(2, {
          message: "Plate not valid",
        })
        .max(20),
      password: z.string().min(2, {
        message: "Model not valid",
      }),
      email: z.string().email({
        message: "Email not valid",
      }),
      is_superuser: z.boolean(),
      type: z.string(),
      name: z.string().optional(),
      code_officer: z.string().optional(),
    })
    .refine(
      (data) => {
        if (data.type === "policy") {
          return !!data.code_officer;
        }
        return true;
      },
      {
        message: "Code oficial required",
        path: ["code_officer"],
      }
    )
    .refine(
      (data) => {
        if (data.type === "policy") {
          return !!data.name;
        }
        return true;
      },
      {
        message: "Name oficial required",
        path: ["name"],
      }
    );

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      password: "",
      email: "",
      username: "",
      is_superuser: false,
      type: "user",
      name: "",
      code_officer: `${getRandomInt()}${getRandomInt()}`,
    },
  });
  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      const data = await createUser(values);
      userStore.getState().addUser(data);
      toast({
        title: "User register success",
        className: "bg-slate-900 text-white",
        duration: 900,
      });
      form.reset();
      setOpen(false);
    } catch (error) {
      toast({
        title: "Error register user",
        className: "bg-red-500 text-white",
        duration: 1000,
      });
    }
  }

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Button>Add User</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Add User</DialogTitle>
          <DialogDescription>Register user and policy</DialogDescription>
        </DialogHeader>
        <div className="grid">
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-2">
              <FormField
                control={form.control}
                name="username"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Username</FormLabel>
                    <FormControl>
                      <Input placeholder="user.code" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="email"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Email</FormLabel>
                    <FormControl>
                      <Input
                        type="email"
                        placeholder="mail@mail.com"
                        {...field}
                      />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
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
              <FormField
                control={form.control}
                name="type"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>User Type</FormLabel>
                    <Select
                      onValueChange={field.onChange}
                      defaultValue={field.value}
                    >
                      <FormControl>
                        <SelectTrigger>
                          <SelectValue placeholder="Select user type" />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        <SelectItem value="user">User</SelectItem>
                        <SelectItem value="policy">Oficial</SelectItem>
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="is_superuser"
                render={({ field }) => (
                  <FormItem className="flex flex-row items-start space-x-3 space-y-0 rounded-md py-4">
                    <FormControl>
                      <Checkbox
                        checked={field.value}
                        onCheckedChange={field.onChange}
                      />
                    </FormControl>
                    <div className="space-y-1 leading-none">
                      <FormLabel>Superuser</FormLabel>
                    </div>
                  </FormItem>
                )}
              />
              {form.control._formValues.type === "policy" && (
                <>
                  <FormField
                    control={form.control}
                    name="code_officer"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Code Oficial</FormLabel>
                        <FormControl>
                          <Input
                            disabled
                            type="number"
                            placeholder="22341123"
                            {...field}
                          />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                  <FormField
                    control={form.control}
                    name="name"
                    render={({ field }) => (
                      <FormItem>
                        <FormLabel>Name Oficial</FormLabel>
                        <FormControl>
                          <Input type="text" placeholder="Dany.js" {...field} />
                        </FormControl>
                        <FormMessage />
                      </FormItem>
                    )}
                  />
                </>
              )}
              <DialogFooter className="mt-4 sm:justify-end">
                <Button type="submit">Save</Button>
              </DialogFooter>
            </form>
          </Form>
        </div>
      </DialogContent>
    </Dialog>
  );
};
