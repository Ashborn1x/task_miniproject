<template>
  <div class="register">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Register</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import api from "@/api"; // axios instance

export default {
  data() {
    return {
      username: "",
      password: "",
      error: null,
    };
  },
  methods: {
    async register() {
      try {
        const res = await api.post("/register", {
          username: this.username,
          password: this.password,
        });
        console.log(res.data);
        alert("Registration successful!");
        this.$router.push("/login");
      } catch (err) {
        console.error(err.response?.data);
        this.error = err.response?.data?.msg || "Registration failed";
      }
    },
  },
};
</script>
