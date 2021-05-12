import { Doughnut, mixins } from "vue-chartjs";

export default {
  extends: Doughnut,
  mixins: [mixins.reactiveProp],
  props: ["data", "options"],
  mounted() {
    this.renderChart(this.data, this.options);
  }
};
