import { create } from "zustand";
import { persist } from "zustand/middleware";
type Store = {
  vehicles: any;
};

const initialState: Store = {
  vehicles: [],
};

type Actions = {
  addVehicle: (vehicle: any) => void;
  setVehicles: (vehicles: []) => void;
  reset: () => void;
};

type StoreWithActions = Store & Actions;

export const vehicleStore = create(
  persist<StoreWithActions>(
    (set) => ({
      ...initialState,
      addVehicle: (vehicle) =>
        set((state) => {
          if (vehicle) {
            return { vehicles: [...state.vehicles, vehicle] };
          }
          return state;
        }),
      setVehicles: (vehicles) =>
        set(() => {
          return {
            vehicles,
          };
        }),
      reset: () => set(initialState),
    }),
    { name: "vehicles" }
  )
);
