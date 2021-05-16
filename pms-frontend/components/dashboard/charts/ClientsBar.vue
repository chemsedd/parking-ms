<template>
  <card class="shadow-card">
    <c-bar :chartData="{}" :data="barData" />
  </card>
</template>

<script>
export default {
  data() {
    return {
      barData: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
        ],
        datasets: [
          {
            label: "Total number of clients",
            backgroundColor: "#f87979",
            data: [40, 20, 22, 39, 40, 40, 39, 30, 40, 20, 52, 21],
          },
        ],
      },
    };
  },
};
</script>

<style>
</style>