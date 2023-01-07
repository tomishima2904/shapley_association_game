/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/templates/*.{html,js}",
    "./static/js/*",
    "./node_modules/flowbite/**/*.js"
],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
