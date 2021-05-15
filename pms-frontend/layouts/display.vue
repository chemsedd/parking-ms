<template>
  <div class="w-screen h-screen flex flex-col">
    <header class="display-header">
      <h1 class="text-orange-700">Display 1</h1>
    </header>
    <main class="display-main"><Nuxt /></main>
    <footer class="display-footer">
      <div>PMS &copy;</div>
      <span>Built by Chems Eddine - 2021.</span>
    </footer>
  </div>
</template>

<script>
export default {};
</script>

<style>
.flex-center-between {
  @apply flex items-center justify-between py-4 px-10;
}

.display-header {
  @apply flex-center-between bg-light-orange uppercase;
}

.display-main {
  @apply w-full h-full flex flex-1;
}

.display-footer {
  @apply flex-center-between bg-dark-blue text-gray-500 font-thin;
}
</style>