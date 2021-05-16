<template>
  <div class="secondary-section gird-cols-2">
    <h3 class="col-span-3">Charts</h3>
    <CClientsBar />
    <CLotsDoughnut />
    <CClientsLine />
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: "Statistics",
    };
  },
  layout: "dashboard",
};
</script>

<style>
</style>