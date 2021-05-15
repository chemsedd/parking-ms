<template>
  <card>
    <CLine :chartData="{}" :data="LineData" />
  </card>
</template>

<script>
export default {
  data() {
    return {
      LineData: {
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
            backgroundColor: "#f8797900",
            borderColor: "#3af47b",
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