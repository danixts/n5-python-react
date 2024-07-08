import api from "./api";

export const loginService = async (body: any) => {
  try {
    const { data } = await api.post("/auth/login", { ...body });
    return data.data;
  } catch (error) {
    throw error;
  }
};

export const getVehicles = async () => {
  try {
    const { data } = await api.get("/vehicle");
    return data.data;
  } catch (error) {
    throw error;
  }
};

export const createVehicle = async (body: any) => {
  try {
    const { data } = await api.post("/vehicle", { ...body });
    return data.data;
  } catch (error) {
    throw error;
  }
};

export const getAllUsers = async () => {
  try {
    const { data } = await api.get("/user/all");
    return data.data;
  } catch (error) {
    throw error;
  }
};

export const createUser = async (body: any) => {
  try {
    const { data } = await api.post("/user", { ...body });
    return data.data;
  } catch (error) {
    throw error;
  }
};

export const dowloadService = async (body: any) => {
  try {
    debugger;
    const params = {
      email: body.email,
      type_report: body.type_report,
    };
    const { data } = await api.get("/infraction/downloadReport", { params });
    return data;
  } catch (error) {
    throw error;
  }
};

export const createInfraction = async (body: any) => {
  try {
    const { data } = await api.post("/infraction", { ...body });
    return data.data;
  } catch (error) {
    throw error;
  }
};

export const getAllInfractions = async (email: string | undefined) => {
  try {
    const params = {
      email,
    };
    const { data } = await api.get("/infraction/all", {params});
    return data.data;
  } catch (error) {
    throw error;
  }
};
