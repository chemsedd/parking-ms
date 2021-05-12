<template>
  <div id="dashboard-container" class="w-screen min-h-screen flex">
    <SideBar />
    <div class="flex flex-col gap-y-2 w-full bg-gray-100 p-12">
      <header class="header-section">
        <h2>Dashboard</h2>
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
      <hr />
      <Nuxt />
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      titleTemplate: (titleChunk) => {
        return titleChunk ? `${titleChunk} | PMS Dashboard` : "PMS | Dashboard";
      },
    };
  },
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
.header-section {
  @apply inline-flex justify-between items-center w-full;
}
</style>
