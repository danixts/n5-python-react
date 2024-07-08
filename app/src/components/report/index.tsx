import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "../ui/form";
import { Input } from "../ui/input";
import {
  Select,
  SelectContent,
  SelectTrigger,
  SelectValue,
  SelectItem,
} from "../ui/select";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { DialogFooter } from "../ui/dialog";
import { Card, CardContent, CardHeader, CardTitle } from "../ui/card";
import { Download } from "lucide-react";
import { useDownload } from "@/hooks/useDowload";
import { Toaster } from "../ui/toaster";
import { useToast } from "../ui/use-toast";
import { dowloadService } from "@/services/service";
export const ReportPage = () => {
  const dowload = useDownload()
  const { toast } = useToast();
  const formSchema = z.object({
    email: z.string().email(),
    type_report: z.string(),
  });

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      email: "",
      type_report: "csv",
    },
  });
  async function onSubmit(values: z.infer<typeof formSchema>) {
    try {
      debugger
      const data = await dowloadService(values);
      toast({
        title: "User register success",
        className: "bg-slate-900 text-white",
        duration: 900,
      });
      dowload(data, values.type_report)
    } catch (error) {
      toast({
        title: "Error report dowload",
        className: "bg-red-500 text-white",
        duration: 1000,
      });
    }
  }
  return (
    <div className="">
      <div className="container flex justify-center items-center h-lvh w-full ">
        <div className="flex flex-col items-center space-y-6">
          <Card x-chunk="dashboard-07-chunk-3" className="">
            <CardHeader>
              <CardTitle className="text-center">Generate report</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid gap-6">
                <div className="grid gap-3">
                  <Form {...form}>
                    <form
                      onSubmit={form.handleSubmit(onSubmit)}
                      className="space-y-2"
                    >
                      <FormField
                        control={form.control}
                        name="email"
                        render={({ field }) => (
                          <FormItem>
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
                        name="type_report"
                        render={({ field }) => (
                          <FormItem>
                            <Select
                              onValueChange={field.onChange}
                              defaultValue={field.value}
                            >
                              <FormControl>
                                <SelectTrigger>
                                  <SelectValue placeholder="Select report type" />
                                </SelectTrigger>
                              </FormControl>
                              <SelectContent>
                                <SelectItem value="csv">CSV</SelectItem>
                                <SelectItem value="json">JSON</SelectItem>
                              </SelectContent>
                            </Select>
                            <FormMessage />
                          </FormItem>
                        )}
                      />
                      <DialogFooter className="mt-4 w-full">
                        <Button className="w-full mt-2 flex items-center justify-center space-x-2" type="submit"> <Download size={18}/> <span>Download report</span></Button>
                      </DialogFooter>
                    </form>
                  </Form>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
      <Toaster />
    </div>
  );
};
