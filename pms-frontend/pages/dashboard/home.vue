<template>
  <main class="main-section">
    <div class="secondary-section">
      <h3 class="col-span-3">Parking lots status</h3>
      <db-lots-card class="shadow-card" />
      <db-lots-card class="shadow-card" />
      <db-lots-card class="shadow-card" />
      <h3 class="col-span-3">Table data</h3>
      <div class="col-span-3">
        <!-- api-url="https://vuetable.ratiw.net/api/users" -->
        <vuetable
          ref="vuetable"
          :fields="fields"
          :api-mode="false"
          :data="users"
        >
        </vuetable>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  head() {
    return {
      title: "Home",
    };
  },
  layout: "dashboard",
  data() {
    return {
      fields: [
        {
          name: "name",
          sortField: "name",
          title: "First name",
          titleClass: "table-header",
          dataClass: "table-data",
        },
        {
          name: "email",
          title: "Email Address",
          titleClass: "table-header",
          dataClass: "table-data",
        },
        {
          name: "birthdate",
          sortField: "birthdate",
          titleClass: "table-header",
          dataClass: "table-data",
        },
        {
          name: "gender",
          sortField: "gender",
          titleClass: "table-header",
          dataClass: "table-data",
          formatter(value) {
            return value === "M" ? "Male" : "Female";
          },
        },
      ],
      users: [
        {
          name: "Edward Elrik",
          nickname: "Fullmetal",
        },
        {
          name: "Naruto",
          nickname: "Uzumaki",
        },
      ],
    };
  },
};
</script>

<style>
.table-header {
  @apply bg-light-orange text-white font-bold p-4 border-4 border-gray-100;
}

.table-data {
  @apply bg-dark-blue text-white p-4;
}
</style>