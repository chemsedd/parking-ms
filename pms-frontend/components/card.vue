<template>
  <div class="card bg-white">
    <slot></slot>
  </div>
</template>

<script>
export default {};
</script>

<style>
.card {
  @apply flex flex-col gap-y-2 rounded-xl shadow-md px-6 py-4 border-b-4;
}
</style>