<template>
  <nuxt-link :to="to" class="card-box">
    <div class="card-body dark-card">
      <slot></slot>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  props: {
    to: String,
  },
};
</script>

<style>
</style>