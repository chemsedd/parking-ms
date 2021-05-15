<template>
  <nuxt-link :to="`/display/${title}`" target="_blank" class="display-card">
    <main class="display-card-body">
      <span class="text-orange-400"
        ><v-icon name="desktop" class="h-4 w-auto" /> {{ _id }}</span
      >
      <h4 class="uppercase text-xl font-black text-light-orange">
        {{ title }}
      </h4>
      <hr class="opacity-20" />
      <p>{{ desc }}</p>
    </main>
  </nuxt-link>
</template>

<script>
export default {
  props: {
    _id: String,
    title: String,
    desc: String,
  },
};
</script>

<style>
.display-card {
  @apply border-8 border-transparent p-1 rounded-3xl;
  &:hover {
    @apply border-light-orange;
  }
}

.display-card-body {
  @apply flex flex-col gap-y-2 rounded-xl px-6 py-4 bg-dark-blue text-white;
}
</style>