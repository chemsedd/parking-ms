<template>
  <div class="w-screen min-h-screen flex flex-col justify-between">
    <Nuxt />
  </div>
</template>
<script>
export default {
  head() {
    return {
      titleTemplate: (titleChunk) => {
        return titleChunk
          ? `${titleChunk} | Parking Management System`
          : "PMS | Parking Management System";
      },
    };
  },
};
</script>

<style>
</style>
