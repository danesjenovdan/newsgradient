module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'airbnb-base',
    'plugin:vue/vue3-recommended',
    'plugin:prettier/recommended',
    'plugin:@nativescript/recommended',
  ],
  plugins: ['vue', 'prettier', '@nativescript'],
  rules: {
    'vue/attribute-hyphenation': 'off',
  },
};
