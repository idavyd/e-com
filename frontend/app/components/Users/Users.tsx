'use client';

import { fetchUsers, IUser } from '@/api/users';
import axios from 'axios';
import { useEffect, useState } from 'react';

export const Users = () => {
  const [users, setUsers] = useState<IUser[]>([]);

  useEffect(() => {
    const getData = async () => {
      try {
        const response = await fetchUsers();
        setUsers(response);
      } catch (error) {
        console.error(error);
      }
    };
    getData();

    console.log(axios.defaults.baseURL);
  }, []);
  return (
    <div>
      {users.map((user) => (
        <div key={user.id}>
          <h2>{user.username}</h2>
        </div>
      ))}
    </div>
  );
};
