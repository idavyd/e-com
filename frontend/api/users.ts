import { axiosInstance } from './axios';

export interface IUser {
  id: number;
  username: string;
}

export const fetchUsers = async () => {
  const response = await axiosInstance.get<IUser[]>('/users');
  return response.data;
};
