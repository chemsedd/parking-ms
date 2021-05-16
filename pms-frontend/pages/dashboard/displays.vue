<template>
  <main class="main-section">
    <div class="secondary-section">
      <h3 class="col-span-3">List of displays</h3>
      <db-display-card
        v-for="display in displays"
        :key="display.id"
        :_id="display._id"
        :title="display.title"
        :desc="display.desc"
      ></db-display-card>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "Displays",
    };
  },
  layout: "dashboard",
  data() {
    return {
      displays: [
        {
          _id: "1",
          title: "ticket",
          desc:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit, sunt!",
        },
        {
          _id: "2",
          title: "map",
          desc:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit, sunt!",
        },
        {
          _id: "3",
          title: "cameras",
          desc:
            "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit, sunt!",
        },
      ],
    };
  },
};
</script>

<style>
</style>