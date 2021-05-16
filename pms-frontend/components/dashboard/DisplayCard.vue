<template>
  <link-card :to="`/display/${title}`">
    <span class="text-orange-400"
      ><v-icon name="desktop" class="h-4 w-auto" /> {{ _id }}</span
    >
    <h4 class="uppercase text-xl font-black text-light-orange">
      {{ title }}
    </h4>
    <hr class="opacity-20" />
    <p>{{ desc }}</p>
  </link-card>
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
</style>