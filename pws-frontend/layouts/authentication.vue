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
html {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, "Helvetica Neue", Arial, sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
}
</style>
