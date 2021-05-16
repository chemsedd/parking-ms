<template>
  <div class="min-w-screen min-h-screen flex flex-col">
    <header class="display-header text-orange-700">
      <h1 class="">Display 1</h1>
      <div class="space-x-2">
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
    <main class="display-main"><Nuxt /></main>
    <footer class="display-footer">
      <div>PMS &copy;</div>
      <span>Built by Chems Eddine - 2021.</span>
    </footer>
  </div>
</template>

<script>
export default {
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
.flex-center-between {
  @apply flex items-center justify-between py-4 px-10;
}

.display-header {
  @apply flex-center-between bg-light-orange uppercase;
}

.display-main {
  @apply flex flex-1;
}

.display-footer {
  @apply flex-center-between bg-dark-blue text-gray-500 font-thin;
}
</style>