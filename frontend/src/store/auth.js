import { defineStore } from "pinia";
import axios from "axios";

const baseUrl = `${import.meta.env.VITE_SERVER_NAME}/users`;

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    // initialize state from local storage to enable user to stay logged in
    user: JSON.parse(localStorage.getItem("user")),
    token: JSON.parse(localStorage.getItem("token")),
  }),
  actions: {
    async login(username, password) {
      var data = {
        grant_type: "",
        username: username,
        password: password,
        scope: "",
        client_id: "",
        client_secret: "",
      };
      var config = {
        method: "post",
        url: import.meta.env.VITE_SERVER_NAME + "login/access-token",
        headers: {
          accept: "application/json",
          "Content-Type": "application/x-www-form-urlencoded",
        },
        data: data,
      };

      const userResponse = await axios.post(
        import.meta.env.VITE_SERVER_NAME + "users/open/email",
        {email: username}
      );

      if (userResponse.data == 1) {
        const response = await axios(config);

        this.user = response.data.user;
        this.token = response.data.access_token;
        // store user details and jwt in local storage to keep user logged in between page refreshes
        localStorage.setItem("user", JSON.stringify(this.user));
        localStorage.setItem("token", JSON.stringify(this.token));
        // redirect to previous url or default to home page
        return userResponse.data;
      } else {
        return userResponse.data;
      }

      // update pinia state
    },
    logout() {
      this.user = null;
      localStorage.removeItem("user");
      localStorage.removeItem("token");
    },
  },
});
