<template>
  <div
    class="w-full grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-2 px-10 py-6"
  >
    <card
      v-for="lot in lots"
      :key="lot.id"
      :class="`${
        lot.status == 0 ? 'green' : lot.status == 1 ? 'dark' : 'red'
      }-card lot-card`"
    >
      <h5 class="text-2xl font-extrabold">
        Lot {{ lot.section }}/{{ lot.id }}
      </h5>
      <div class="inline-flex flex-1 items-center justify-between">
        <span>{{
          lot.status == 0
            ? "Free"
            : lot.status == 1
            ? "Occupied"
            : "Out of service"
        }}</span>
        <div v-if="lot.status == 1" class="space-x-1">
          <v-icon name="car-alt" class="w-6 h-6" />
          <span class="text-light-orange text-2xl font-black">{{
            lot.car
          }}</span>
        </div>
      </div>
    </card>
  </div>
</template>

<script>
export default {
  layout: "display",
  data() {
    return {
      lots: [
        {
          section: "A",
          id: "1",
          status: "0",
          car: "",
        },
        {
          section: "A",
          id: "2",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "3",
          status: "-1",
          car: "",
        },
        {
          section: "A",
          id: "4",
          status: "-1",
          car: "",
        },
        {
          section: "A",
          id: "5",
          status: "0",
          car: "",
        },
        {
          section: "A",
          id: "6",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "7",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "8",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "9",
          status: "0",
          car: "",
        },
        {
          section: "A",
          id: "10",
          status: "0",
          car: "",
        },
        {
          section: "A",
          id: "11",
          status: "0",
          car: "",
        },
        {
          section: "A",
          id: "12",
          status: "0",
          car: "",
        },
        {
          section: "A",
          id: "13",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "14",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "15",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "16",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "17",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "18",
          status: "1",
          car: "FX04",
        },
        {
          section: "A",
          id: "19",
          status: "1",
          car: "FX04",
        },
      ],
    };
  },
};
</script>

<style scoped>
.lot-card {
  @apply rounded-none h-full font-semibold italic;
}

.green-card h5 {
  @apply text-lime-600;
}

.dark-card h5 {
  @apply text-light-orange;
}
</style>