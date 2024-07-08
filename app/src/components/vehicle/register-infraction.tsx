import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogClose,
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
import { createInfraction, createVehicle } from "@/services/service";
import { vehicleStore } from "@/store/vehicleStore";
import { useToast } from "../ui/use-toast";
import { FC } from "react";
import { useAuthStore } from "@/store/authStore";
export const FormRegisterInfraction: FC<{
  open: boolean;
  setOpen: any;
  vehicle: any;
}> = ({ open, setOpen, vehicle }) => {
  const { toast } = useToast();
  const formSchema = z.object({
    comments: z.string().max(100),
  });

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      comments: "",
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      const userId = useAuthStore.getState().userInfo?.id;
      const body = {
        comments: values.comments,
        state: true,
        timestamp: new Date(),
        vehicle_id: vehicle.id,
        police_id: userId,
      };
      console.log({body});
      await createInfraction(body);
      toast({
        title: "Register infraction user",
        className: "bg-slate-900 text-white",
        duration: 900,
      });
      form.reset();
    } catch (error) {
      toast({
        title: "Error save infraction",
        className: "bg-red-500 text-white",
        duration: 1000,
      });
    }
  }
  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Register infraction</DialogTitle>
          <DialogDescription>Register infraction oficial</DialogDescription>
        </DialogHeader>
        <div className="grid">
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-2">
              <FormField
                control={form.control}
                name="comments"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Comment</FormLabel>
                    <FormControl>
                      <Input placeholder="Commnets..." {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <DialogFooter className="mt-4 sm:justify-end">
                <DialogClose asChild>
                  <Button type="submit">Save</Button>
                </DialogClose>
              </DialogFooter>
            </form>
          </Form>
        </div>
      </DialogContent>
    </Dialog>
  );
};
