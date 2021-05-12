<template>
  <vuetable
    ref="vuetable"
    api-url="https://vuetable.ratiw.net/api/users"
    :fields="['name', 'nickname', 'email', 'gender']"
    data-path=""
    pagination-path=""
  >
  </vuetable>
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