<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-sm bg-white p-6 rounded-xl shadow-md">
      <h2 class="text-2xl font-bold mb-4 text-center">Login</h2>

      <form @submit.prevent="handleLogin">
        <input
          v-model="username"
          type="text"
          placeholder="Username"
          class="w-full border p-2 rounded mb-3"
        />
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          class="w-full border p-2 rounded mb-3"
        />
        <button
          type="submit"
          class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
        >
          Login
        </button>
      </form>

      <!-- error message -->
      <p v-if="error" class="text-red-500 mt-3 text-center">{{ error }}</p>

      <!-- success message -->
      <p v-if="success" class="text-green-600 mt-3 text-center font-semibold">
        {{ success }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "@/api";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const error = ref("");
const success = ref("");
const router = useRouter();

const handleLogin = async () => {
  error.value = "";
  success.value = "";

  try {
    const res = await api.post("/login", {
      username: username.value,
      password: password.value,
    });

    if (res.data.token) {
      localStorage.setItem("token", res.data.token);
      success.value = "Login successful 🎉 Redirecting...";
      setTimeout(() => {
        router.push("/tasks");
      }, 1000); // wait 1s before redirect
    } else {
      error.value = "Login failed. No token received.";
    }
  } catch (err) {
    console.error("Login error:", err.response?.data || err.message);
    error.value = err.response?.data?.msg || "Invalid username or password";
  }
};
</script>
