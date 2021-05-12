<template>
  <main class="main-section">
    <div class="secondary-section">
      <h3 class="col-span-3">Charts</h3>
      <db-lots-card />
      <db-lots-card />
      <db-lots-card />
      <hr class="col-span-3" />
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
</style>