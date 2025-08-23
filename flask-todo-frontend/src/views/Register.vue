<template>
  <div class="flex min-h-screen">
    <!-- Left side with gradient / branding -->
    <div class="hidden lg:flex flex-col justify-center items-center w-1/2 bg-gradient-to-br from-indigo-600 via-blue-500 to-purple-600 text-white p-12">
      <h1 class="text-4xl font-extrabold mb-4">🚀 MyTodo</h1>
      <p class="text-lg text-indigo-100 max-w-sm text-center">
        Create an account and start managing your tasks today.
      </p>
    </div>

    <!-- Right side register form -->
    <div class="flex flex-1 justify-center items-center bg-gray-50">
      <div class="w-full max-w-md bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition">
        <h2 class="text-3xl font-extrabold mb-6 text-center text-gray-800">Create Account ✨</h2>

        <form @submit.prevent="register" class="space-y-5">
          <div>
            <label class="block mb-1 text-sm font-medium text-gray-700">Username</label>
            <input
              v-model="username"
              type="text"
              placeholder="Enter your username"
              class="w-full border border-gray-300 focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 p-3 rounded-lg outline-none transition"
            />
          </div>

          <div>
            <label class="block mb-1 text-sm font-medium text-gray-700">Password</label>
            <input
              v-model="password"
              type="password"
              placeholder="••••••••"
              class="w-full border border-gray-300 focus:ring-2 focus:ring-indigo-400 focus:border-indigo-400 p-3 rounded-lg outline-none transition"
            />
          </div>

          <button
            type="submit"
            class="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 active:scale-95 transition"
          >
            Register
          </button>
        </form>

        <!-- error message -->
        <p v-if="error" class="text-red-500 mt-4 text-center font-medium">
          {{ error }}
        </p>

        <p class="mt-6 text-sm text-center text-gray-600">
          Already have an account?
          <RouterLink to="/login" class="text-indigo-600 hover:underline"> Sign in</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "@/api";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const error = ref(null);
const router = useRouter();

const register = async () => {
  error.value = null;

  try {
    const res = await api.post("/register", {
      username: username.value,
      password: password.value,
    });

    console.log(res.data);
    alert("Registration successful!");
    router.push("/login");
  } catch (err) {
    console.error(err.response?.data);
    error.value = err.response?.data?.msg || "Registration failed";
  }
};
</script>
