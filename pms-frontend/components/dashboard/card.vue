<template>
  <div class="card bg-white border-red-600">
    <header class="inline-flex gap-x-2">
      <v-icon name="car" class="w-5 h-auto text-orange-500" />
      <h3>Parking Lots</h3>
    </header>
    <hr />
    <dl>
      <dt>Total lots:</dt>
      <dd class="text-blue-600">100</dd>
      <dt>Occupied Lots:</dt>
      <dd class="text-red-600">25</dd>
      <dt>Empty lots:</dt>
      <dd class="text-green-600">75</dd>
    </dl>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.card {
  @apply flex flex-col gap-y-2 rounded-xl shadow-md px-6 py-4 border-b-4;
}

dl {
  @apply grid grid-cols-2;
}

dt {
  @apply text-gray-800;
}

dd {
  @apply text-right font-bold;
}
</style>