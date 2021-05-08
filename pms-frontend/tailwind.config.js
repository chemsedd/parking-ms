// tailwind.config.js
const colors = require("tailwindcss/colors");

module.exports = {
  purge: [
    "./components/**/*.{vue,js}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}"
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        orange: colors.orange,
        cyan: colors.cyan,
        "light-blue": colors.lightBlue
      }
    }
  },
  variants: {
    extend: {
      borderWidth: ["hover", "focus"],
      appearance: ["active", "focus"]
    }
  },
  plugins: []
};
