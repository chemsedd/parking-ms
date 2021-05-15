<template>
  <div class="w-screen h-screen flex items-center justify-between">
    <div
      class="w-full md:w-1/2 h-full flex flex-col items-center justify-between bg-gray-100"
    >
      <div class="w-full h-1/3 flex items-center gap-x-4 p-16">
        <logo width="20" height="full" />
        <div>
          <h1 class="text-4xl font-bold text-light-orange">
            Parking Management System
          </h1>
          <p>PMS is a tool for managing your parking lots in an easy way!</p>
        </div>
      </div>
      <!-- Login form -->
      <div class="w-full max-w-xl h-2/3 flex place-content-center py-8 px-20">
        <form action="POST" class="w-2/3 flex flex-col gap-y-4">
          <!-- Username -->
          <div class="input-section">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" />
          </div>
          <!-- Password -->
          <div class="input-section">
            <label for="password">Passowrd</label>
            <input type="password" id="password" name="password" />
          </div>
          <div>
            <button class="btn--primary w-full" @click.prevent="">Login</button>
          </div>
        </form>
      </div>
      <!-- Footer -->
      <footer
        class="min-w-full h-12 flex items-center justify-between bg-light-orange text-orange-200 font-thin p-4"
      >
        <span>Parking Management System</span>
        <p>Copyrights reserved &copy; 2021.</p>
      </footer>
    </div>
    <div class="hidden md:block w-1/2 h-full">
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
      title: "Login",
    };
  },
};
</script>

<style>
</style>
