<template>
  <div class="p-4">
    <h1 class="text-xl font-bold mb-4">My Tasks</h1>

    <!-- Add Task -->
    <form @submit.prevent="addTask" class="mb-4">
      <input v-model="newTask" placeholder="New Task" class="border p-2 mr-2" />
      <button class="bg-blue-500 text-white px-4 py-2">Add</button>
    </form>

    <!-- Task List -->
    <ul>
      <li v-for="task in tasks" :key="task.id" class="flex items-center justify-between border-b py-2">
        <span :class="{ 'line-through': task.completed }">{{ task.title }}</span>
        <div>
          <button @click="toggleTask(task)" class="bg-yellow-500 text-white px-2 py-1 mr-2">
            {{ task.completed ? "Undo" : "Done" }}
          </button>
          <button @click="deleteTask(task.id)" class="bg-red-500 text-white px-2 py-1">Delete</button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import api from "../api";

export default {
  data() {
    return {
      tasks: [],
      newTask: "",
    };
  },
  async created() {
    this.fetchTasks();
  },
  methods: {
    async fetchTasks() {
      try {
        const res = await api.get("/tasks");
        this.tasks = res.data;
      } catch (err) {
        console.error(err);
      }
    },
    async addTask() {
      if (!this.newTask) return;
      try {
        const res = await api.post("/tasks", { title: this.newTask });
        this.tasks.push(res.data);
        this.newTask = "";
      } catch (err) {
        console.error(err);
      }
    },
    async toggleTask(task) {
      try {
        const res = await api.put(`/tasks/${task.id}`, {
          title: task.title,
          completed: !task.completed,
        });
        task.completed = res.data.completed;
      } catch (err) {
        console.error(err);
      }
    },
    async deleteTask(id) {
      try {
        await api.delete(`/tasks/${id}`);
        this.tasks = this.tasks.filter((t) => t.id !== id);
      } catch (err) {
        console.error(err);
      }
    },
  },
};
</script>
