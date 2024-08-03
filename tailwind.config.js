/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./resources/templates/**/*.html",
    "./resources/templates/*.html",
    "./resources/static/**/*.{css, scss, js}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#42b883",
        "secondary-dark": "#272932",
        "primary-dark": "#2b2d42",
        "body-dark": "#242938",
        gray: { DEFAULT: "#394E6A", dark: "#414558" },
        light: "#f7f7fa",
      },
    },
    fontFamily: {
      display: ["Poppins", "sans-serif"],
    },
  },
  plugins: [],
};
