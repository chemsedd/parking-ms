<template>
  <div class="w-screen h-screen flex items-center justify-between">
    <div
      class="w-1/2 h-full flex items-center justify-between flex-col bg-gray-100"
    >
      <div>
        <h1 class="text-4xl font-bold text-orange-500">
          Parking Management System
        </h1>
        <p>PMS is a tool for managing your parking lots in an easy way!</p>
      </div>
      <!-- Login form -->
      <div>
        <form action="POST" class="flex flex-col gap-y-4">
          <!-- Username -->

          <div class="input-section">
            <label for="username">Username</label>
            <input type="text" name="username" />
          </div>
          <!-- Password -->
          <div class="input-section">
            <label for="password">Username</label>
            <input type="password" name="password" />
          </div>
        </form>
      </div>
      <!-- Footer -->
      <footer
        class="min-w-full h-12 container bg-orange-600 text-white font-thin"
      >
        <p>Copyrights reserved &copy; 2021.</p>
      </footer>
    </div>
    <div class="w-1/2 h-full">
      <img
        class="w-full h-full object-cover"
        src="~/assets/images/parking-pic.jpg"
        alt="Parking Lots"
      />
    </div>
  </div>
</template>

<script>
export default {
  layout: "authentication",
  head() {
    return {
      title: "Sign up",
    };
  },
};
</script>

<style>
</style>
