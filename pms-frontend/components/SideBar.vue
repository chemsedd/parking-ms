<template>
  <div :class="`${toggle ? 'w-80' : 'w-28'} sidebar`">
    <!-- Toggle sidebar -->
    <button class="btn-sm toggle-btn" @click="toggle = !toggle">
      <v-icon
        :name="toggle ? 'angle-left' : 'angle-right'"
        class="w-5 h-5 text-white"
      />
    </button>
    <!-- Title -->
    <div class="title-section">
      <img
        class="w-12 h-12"
        src="~/assets/images/pms-logo.svg"
        alt="Parmking Management System logo"
      />
      <h1 class="title">PMS</h1>
    </div>
    <hr class="border-light-orange opacity-50 w-1/2 mx-auto" />
    <!-- User infos (picture, name...) -->
    <div class="user-section">
      <img
        src="~/assets/images/user.jpg"
        alt="User image"
        :class="`${toggle ? 'w-20 h-20' : 'w-10 h-10'} user-image`"
      />
      <span :class="`${toggle ? 'block' : 'hidden'} user-name`">
        Chems Eddine Senoussi
      </span>
    </div>
    <!-- Menu section -->
    <ul class="menu-section">
      <li v-for="(icon, label) in menu" :key="label">
        <button class="btn sidebar-menu-btn">
          <v-icon :name="icon" class="w-5 h-5" />
          <span :class="`${toggle ? 'block' : 'hidden'}`">{{
            label | capitalize
          }}</span>
        </button>
      </li>
    </ul>
    <div class="grid grid-cols-3 gap-2">
      <button class="btn flex place-content-center bg-red-500 text-white">
        <v-icon name="power-off" class="w-5 h-6" />
      </button>
      <button class="btn flex place-content-center bg-red-500 text-white">
        <v-icon name="power-off" class="w-5 h-6" />
      </button>
      <button class="btn flex place-content-center bg-red-500 text-white">
        <v-icon name="power-off" class="w-5 h-6" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      toggle: true,
      menu: {
        home: "home",
        statistics: "table",
        settings: "cogs",
      },
    };
  },
};
</script>

<style>
/* Toggle sidebar button */
.toggle-btn {
  @apply p-0 flex items-center justify-center absolute top-2 -right-10 w-8 h-8 bg-dark-blue opacity-20 hover:opacity-100;
}

/* Sidebar */
/* bg-gradient-to-tr from-light-blue-900 to-light-blue-700 */
.sidebar {
  @apply h-screen flex flex-col justify-between space-y-4 bg-dark-blue shadow-lg p-4 relative;
  transition: width 0.2s linear 0s;
}

/* Title section */
.title-section {
  @apply flex flex-col items-center justify-center gap-2;
}

.title {
  font-family: "Open Sans";
  @apply text-white;
}
/* User infos */

.user-section {
  @apply flex flex-col items-center gap-y-2;
}

.user-section .user-image {
  @apply object-cover rounded-md shadow-md;
}

.user-section .user-name {
  @apply text-gray-300 font-light text-sm;
}

.menu-section {
  @apply flex flex-col justify-start gap-y-2 h-full text-white;
}

.sidebar-menu-btn {
  @apply w-full h-10 flex items-center space-x-2 text-xl hover:bg-light-orange;
}
</style>