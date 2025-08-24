<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Navbar -->
    <nav class="bg-white shadow-md">
      <div class="max-w-4xl mx-auto px-4 py-3 flex justify-between items-center">
        <h1 class="text-2xl font-bold text-gray-800">📋 My Tasks</h1>

        <div class="flex items-center space-x-4">
          <!-- User Name -->
          <span class="text-gray-700 font-medium">User</span>

          <!-- Logout Button -->
          <button
            @click="logout"
            class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg font-medium transition"
          >
            Logout
          </button>
        </div>
      </div>
    </nav>

    <!-- Tasks Card -->
    <div class="max-w-2xl mx-auto bg-white shadow-xl rounded-2xl p-6 mt-6">
      <!-- Add Task -->
      <form @submit.prevent="addTask" class="flex mb-6">
        <input
          v-model="newTask"
          placeholder="Add a new task..."
          class="flex-1 border border-gray-300 rounded-l-lg px-4 py-2 focus:ring-2 focus:ring-blue-400 focus:outline-none"
        />
        <button
          class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-r-lg font-medium transition"
        >
          Add
        </button>
      </form>

      <!-- Task List -->
      <ul class="space-y-3">
        <li
          v-for="task in tasks"
          :key="task.id"
          class="flex items-center justify-between bg-gray-100 hover:bg-gray-200 p-4 rounded-lg transition"
        >
          <span
            :class="[ 'text-gray-800 font-medium', { 'line-through text-gray-500 italic': task.completed } ]"
          >
            {{ task.title }}
          </span>
          <div class="flex space-x-2">
            <button
              @click="toggleTask(task)"
              :class="[
                'px-3 py-1 rounded-lg font-medium transition',
                task.completed
                  ? 'bg-yellow-500 hover:bg-yellow-600 text-white'
                  : 'bg-green-500 hover:bg-green-600 text-white'
              ]"
            >
              {{ task.completed ? "Undo" : "Done" }}
            </button>
            <button
              @click="deleteTask(task.id)"
              class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded-lg font-medium transition"
            >
              Delete
            </button>
          </div>
        </li>
      </ul>

      <!-- Empty State -->
      <p
        v-if="tasks.length === 0"
        class="text-center text-gray-500 italic mt-6"
      >
        No tasks yet. Add one above!
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import api from "@/api";

const tasks = ref([]);
const newTask = ref("");
const router = useRouter();

const fetchTasks = async () => {
  try {
    const res = await api.get("/tasks");
    tasks.value = res.data;
  } catch (err) {
    console.error(err);
  }
};

const addTask = async () => {
  if (!newTask.value.trim()) return;
  try {
    const res = await api.post("/tasks", { title: newTask.value });
    tasks.value.push(res.data);
    newTask.value = "";
  } catch (err) {
    console.error(err);
  }
};

const toggleTask = async (task) => {
  try {
    const res = await api.put(`/tasks/${task.id}`, {
      title: task.title,
      completed: !task.completed,
    });
    task.completed = res.data.completed;
  } catch (err) {
    console.error(err);
  }
};

const deleteTask = async (id) => {
  try {
    await api.delete(`/tasks/${id}`);
    tasks.value = tasks.value.filter((t) => t.id !== id);
  } catch (err) {
    console.error(err);
  }
};

const logout = () => {
  localStorage.removeItem("token");
  router.push("/login");
};

onMounted(fetchTasks);
</script>
