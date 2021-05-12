<template>
  <main class="main-section">
    <div class="secondary-section">
      <h3 class="col-span-3">Charts</h3>
      <db-lots-card />
      <db-lots-card />
      <db-lots-card />
    </div>
    <div class="secondary-section">
      <h3 class="col-span-3">Charts</h3>
      <CClientsBar />
      <CLotsDoughnut />
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "Index",
    };
  },
  layout: "dashboard",
  data() {
    return {};
  },
};
</script>

<style>
.main-section {
  @apply flex flex-col gap-8;
}

.secondary-section {
  @apply grid grid-cols-3 gap-x-6 gap-y-3 w-full;
}
</style>