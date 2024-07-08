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
import { createVehicle } from "@/services/service";
import { vehicleStore } from "@/store/vehicleStore";
import { useToast } from "../ui/use-toast";
export const FormVehicle = () => {
  const { toast } = useToast()
  const formSchema = z.object({
    car_plate: z
      .string()
      .min(2, {
        message: "Plate not valid",
      })
      .max(20),
    model: z.string().min(2, {
      message: "Model not valid",
    }),
    color: z.string().min(2, {
      message: "Color not valid",
    }),
  });

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      car_plate: "",
      model: "",
      color: "",
    },
  });

  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      const data = await createVehicle(values)
      vehicleStore.getState().addVehicle(data)
      toast({
        title: "Vehicle register",
        className: "bg-slate-900 text-white",
        duration: 900
      })
      form.reset()
    } catch (error) {
      toast({
        title: "Error Register Vehicle",
        className: "bg-red-500 text-white",
        duration: 1000
      })
    }
  }

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button>Add Vehicle</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>Add Vehicle</DialogTitle>
          <DialogDescription>Register vehicle</DialogDescription>
        </DialogHeader>
        <div className="grid">
          <Form {...form}>
            <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-2">
              <FormField
                control={form.control}
                name="car_plate"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Nro Plate</FormLabel>
                    <FormControl>
                      <Input placeholder="CXX2321" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="color"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Color</FormLabel>
                    <FormControl>
                      <Input placeholder="Verde" {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <FormField
                control={form.control}
                name="model"
                render={({ field }) => (
                  <FormItem>
                    <FormLabel>Model</FormLabel>
                    <FormControl>
                      <Input placeholder="BMW" {...field} />
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
