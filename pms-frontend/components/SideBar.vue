<template>
  <div :class="`${toggle ? 'w-80' : 'w-24'} sidebar`">
    <!-- Toggle sidebar -->
    <button class="btn-sm toggle-btn" @click="toggle = !toggle">
      <v-icon
        :name="toggle ? 'angle-left' : 'angle-right'"
        class="w-5 h-5 text-white"
      />
    </button>
    <!-- Title -->
    <div :class="`title-section ${toggle ? 'flex-row' : 'flex-col'}`">
      <img
        class="w-12 h-12"
        src="~/assets/images/pms-logo.svg"
        alt="Parmking Management System logo"
      />
      <h1 :class="`title ${toggle ? '' : 'text-3xl'}`">PMS</h1>
    </div>
    <hr class="sidebar-hr" />
    <!-- User infos (picture, name...) -->
    <div class="user-section">
      <img src="~/assets/images/user.jpg" alt="User image" class="user-image" />
      <div :class="`${toggle ? 'block' : 'hidden'} flex flex-col`">
        <span class="user-name"> Chems Eddine Senoussi </span>
        <span class="text-green-700 text-sm">◉ Admin</span>
      </div>
    </div>
    <hr class="sidebar-hr" />
    <!-- Menu section -->
    <ul class="menu-section">
      <li v-for="item in menu" :key="item.label">
        <nuxt-link
          :to="{ path: item.link }"
          class="btn sidebar-menu-btn"
          append
        >
          <v-icon :name="item.icon" class="w-5 h-5" />
          <span :class="`${toggle ? 'block' : 'hidden'}`">{{
            item.label
          }}</span>
        </nuxt-link>
      </li>
    </ul>
    <div class="grid grid-cols-3 gap-2">
      <button
        class="btn flex place-content-center hover:border-2 hover:border-light-orange text-light-orange"
      >
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
      menu: [
        {
          label: "Home",
          icon: "home",
          link: "/dashboard/home",
        },
        {
          label: "Statistics",
          icon: "table",
          link: "/dashboard/statistics",
        },
        {
          label: "Settings",
          icon: "cogs",
          link: "/dashboard/settings",
        },
      ],
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
.sidebar {
  @apply h-screen flex flex-col justify-between space-y-4 bg-dark-blue shadow-lg px-4 py-2 relative;
  transition: width 0.2s linear 0s;
}

.sidebar-hr {
  @apply border-light-orange border-dashed opacity-50 w-full;
  opacity: 45%;
}

.nuxt-link-active {
  @apply bg-light-orange;
}

/* Title section */
.title-section {
  @apply flex items-center justify-center gap-2;
}

.title {
  font-family: "Open Sans";
  @apply text-white;
}
/* User infos */

.user-section {
  @apply flex items-center gap-x-2;
}

.user-section .user-image {
  @apply w-16 h-16 object-cover rounded-md shadow-md;
}

.user-section .user-name {
  @apply text-gray-300 font-semibold text-sm;
}

.menu-section {
  @apply flex flex-col justify-start gap-y-2 h-full text-white;
}

.sidebar-menu-btn {
  @apply w-full h-10 flex items-center gap-x-2 text-xl hover:bg-light-orange;
}
</style>