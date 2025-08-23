<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <!-- Navbar -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
      <div class="max-w-6xl mx-auto flex items-center justify-between p-4">
        <!-- Brand -->
        <RouterLink to="/" class="text-2xl font-bold text-blue-600 tracking-wide">
          VueTodo
        </RouterLink>

        <!-- Nav Links -->
        <nav class="space-x-6">
          <RouterLink
            to="/"
            class="text-gray-600 hover:text-blue-600 font-medium transition"
          >
            Home
          </RouterLink>
          <RouterLink
            to="/about"
            class="text-gray-600 hover:text-blue-600 font-medium transition"
          >
            About
          </RouterLink>
          <RouterLink
            to="/login"
            class="text-gray-600 hover:text-blue-600 font-medium transition"
          >
            Login
          </RouterLink>
        </nav>
      </div>
    </header>

    <!-- Page Content -->
    <main class="flex-grow bg-gray-50">
      <RouterView />
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t text-center py-4 text-gray-500 text-sm">
      © 2025 VueTodo · Built with ❤️ using Vue & Flask
    </footer>
  </div>
</template>
