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
        orange: {
          100: "#fffaf0",
          200: "#feebc8",
          300: "#fbd38d",
          400: "#f6ad55",
          500: "#ed8936",
          600: "#dd6b20",
          700: "#c05621",
          800: "#9c4221",
          900: "#7b341e"
        }
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
