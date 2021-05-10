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
    <div :class="`title-section ${toggle ? 'flex-row' : 'flex-col'}`">
      <img
        class="w-12 h-12"
        src="~/assets/images/pms-logo.svg"
        alt="Parmking Management System logo"
      />
      <h1 class="title">PMS</h1>
    </div>
    <hr class="sidebar-hr" />
    <!-- User infos (picture, name...) -->
    <div class="user-section">
      <img
        src="~/assets/images/user.jpg"
        alt="User image"
        :class="`${toggle ? 'w-16 h-16' : 'w-12 h-12'} user-image`"
      />
      <div :class="`${toggle ? 'block' : 'hidden'} flex flex-col`">
        <span class="user-name"> Chems Eddine Senoussi </span>
        <span class="text-green-700 text-sm">◉ Admin</span>
      </div>
    </div>
    <hr class="sidebar-hr" />
    <!-- Menu section -->
    <ul class="menu-section">
      <li v-for="(icon, label) in menu" :key="label">
        <button
          :class="`btn sidebar-menu-btn ${
            label == 'Home' ? 'bg-light-orange' : ''
          }`"
        >
          <v-icon :name="icon" class="w-5 h-5" />
          <span :class="`${toggle ? 'block' : 'hidden'}`">{{ label }}</span>
        </button>
      </li>
    </ul>
    <div class="grid grid-cols-3 gap-2">
      <button
        class="btn flex place-content-center hover:border-2 hover:border-light-orange text-light-orange"
      >
        <v-icon name="power-off" class="w-5 h-6" />
      </button>
      <button
        class="btn flex place-content-center hover:border-2 hover:border-light-orange text-light-orange"
      >
        <v-icon name="power-off" class="w-5 h-6" />
      </button>
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
      menu: {
        Home: "home",
        Statistics: "table",
        Settings: "cogs",
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
.sidebar {
  @apply h-screen flex flex-col justify-between space-y-4 bg-dark-blue shadow-lg px-4 py-2 relative;
  transition: width 0.2s linear 0s;
}

.sidebar-hr {
  @apply border-light-orange border-dashed opacity-50 w-10/12 mx-auto;
  opacity: 45%;
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
  @apply flex items-center gap-x-2 px-4;
}

.user-section .user-image {
  @apply object-cover rounded-md shadow-md;
}

.user-section .user-name {
  @apply text-gray-300 font-semibold text-sm;
}

.menu-section {
  @apply flex flex-col justify-start gap-y-2 h-full text-white;
}

.sidebar-menu-btn {
  @apply w-full h-10 flex items-center space-x-2 text-xl hover:bg-light-orange;
}
</style>