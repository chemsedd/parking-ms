<template>
  <div :class="`${toggle ? 'w-80' : 'w-28'} sidebar`">
    <button class="btn-sm toggle-btn" @click="toggle = !toggle">
      <v-icon name="angle-right" class="w-4 h-4 text-cyan-700" />
    </button>
    <!-- User infos (picture, name...) -->
    <div class="user-section">
      <img
        src="~/assets/images/user.jpg"
        alt="User image"
        :class="`${toggle ? 'w-20 h-20' : 'w-10 h-10'} user-image`"
      />
      <h3 :class="`${toggle ? 'block' : 'hidden'} user-name`">
        Chems Eddine Senoussi
      </h3>
    </div>
    <!-- Menu section -->
    <ul class="menu-section">
      <li v-for="(icon, label) in menu" :key="label">
        <button
          class="btn w-full h-16 flex items-center space-x-2 text-xl bg-cyan-700 hover:bg-cyan-500 shadow-md"
        >
          <v-icon :name="icon" class="w-10 h-10 rounded-full p-2 border-2" />
          <span :class="`${toggle ? 'block' : 'hidden'}`">{{ label }}</span>
        </button>
      </li>
    </ul>
    <div class="grid grid-cols-1">
      <button
        class="btn flex place-content-center bg-red-500 text-white shadow-md"
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
        home: "home",
        settings: "cogs",
      },
    };
  },
};
</script>

<style>
/* Toggle sidebar button */
.toggle-btn {
  @apply absolute top-2 -right-10 w-8 h-8 bg-light-blue-900;
}

/* Sidebar */

.sidebar {
  @apply h-screen flex flex-col justify-between space-y-4 bg-light-blue-900 shadow-md p-4 relative;
  transition: width 0.2s linear 0s;
}

/* User infos */

.user-section {
  @apply flex flex-col items-center gap-y-2;
}

.user-section .user-image {
  @apply object-cover rounded-full shadow-md;
}

.user-section .user-name {
  @apply text-white text-lg font-bold;
}

.menu-section {
  @apply flex flex-col justify-start gap-y-2 h-full text-white;
}
</style>