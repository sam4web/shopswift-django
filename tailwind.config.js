/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./templates/**/*.html",
    "./templates/*.html",
    "./static/**/*.{css, scss, js}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#42b883",
        "secondary-dark": "#021431",
        "primary-dark": "#2b2d42",
        "body-dark": "#242938",
        gray: { DEFAULT: "#394E6A", dark: "#414558" },
        light: "#f0fcfb",
      },
    },
    fontFamily: {
      display: ["Poppins", "sans-serif"],
    },
  },
  plugins: [],
};
