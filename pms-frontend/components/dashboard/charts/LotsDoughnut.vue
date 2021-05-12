<template>
  <card><CDoughnut :chartData="{}" :data="doughnutData" /></card>
</template>

<script>
export default {
  data() {
    return {
      doughnutData: {
        labels: ["Free", "Occupied", "Out of service"],
        datasets: [
          {
            label: "Free",
            backgroundColor: ["#00ed76", "#f87979", "#afafaf"],
            data: [40, 20, 2],
          },
        ],
      },
    };
  },
};
</script>

<style>
</style>