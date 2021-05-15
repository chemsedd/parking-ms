<template>
  <card>
    <header class="inline-flex justify-between gap-x-4">
      <h3>Parking Lots</h3>
      <v-icon name="car" class="w-5 h-auto text-orange-500" />
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
  </card>
</template>

<script>
export default {};
</script>

<style scoped>
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