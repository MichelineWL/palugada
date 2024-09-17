/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
  ],
  theme: {
    extend: {
      colors: {
        'primary-1' : '#234768',
        'light-1' : '#FDF9F0',
        'light-2' : '#8FD4C6',
        'light-3' : '#ABDBFB',
        'light-4' : '#D9D9D9',
        'light-5' : '#DCEEE3',
        'light-6' : '#FEFAEF',
      },
      width: {
        '300' : '300px',
        '350' : '350px',
        '400' : '400px',
        '500' : '500px',
        '600' : '600px',
        '800' : '800px',
        },
        height: {
        '200' : '200px',
        '300' : '300px',
        '500' : '500px',
        '800' : '800px',
      },
    },
  },
  plugins: [],
}
