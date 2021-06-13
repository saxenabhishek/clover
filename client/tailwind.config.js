module.exports = {
  mode: "jit",
  purge: ["./pages/**/*.{js,jsx}", "./components/**/*.{js,jsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        custRed: "#E63946",
        custWhite: "#F1FAEE",
        custBlue: "#a8dadc",
        custBlue2: "#457b9d",
        custBlue3: "#1d3557",
      },
      fontFamily: {
        raleway: ["Raleway", "sans-serif"],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
