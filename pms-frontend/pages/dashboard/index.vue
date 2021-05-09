<template>
  <div class="flex flex-col gap-4">
    <header class="title-section">
      <h2>Parking lots statistics</h2>
      <div
        class="inline-flex gap-x-6 items-center bg-gradient-to-bl from-pink-400 to-orange-600 rounded-md shadow-md px-4 py-2 text-bold text-white"
      >
        <span>
          <v-icon name="calendar-alt" class="w-4 h-4" />
          {{ now }}</span
        >
        <span>
          <v-icon name="clock" class="w-4 h-4" />
          {{ today }}</span
        >
      </div>
    </header>
    <main class="main-section">
      <db-card />
      <db-card />
      <db-card />
    </main>
  </div>
</template>

<script>
export default {
  layout: "dashboard",
  computed: {
    today() {
      var today = new Date();
      return (
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate()
      );
    },
    now() {
      var today = new Date();
      return (
        today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds()
      );
    },
  },
};
</script>

<style>
.title-section {
  @apply inline-flex justify-between items-center;
}

.main-section {
  @apply grid grid-cols-3 gap-2 w-full;
}
</style>