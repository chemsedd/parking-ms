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
        "light-orange": "#FF8D41",
        "dark-blue": "#1C273D",
        orange: colors.orange,
        lime: colors.lime,
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
