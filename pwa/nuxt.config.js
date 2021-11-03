const OG_TITLE = 'Newsgradient'
const OG_DESCRIPTION =
  'Najaktuelnije vijesti u izvještajima bosanskohercegovačkih medija grupisane po ideološkoj orijentaciji.'
const OG_IMAGE = 'https://newsgradient.org/newsgradient-og.jpg'

export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: (titleChunk) => {
      return titleChunk ? `${titleChunk} - Newsgradient` : 'Newsgradient'
    },
    meta: [
      // hid is used as unique identifier; use the same hid if you want to replace the tag in a component
      { hid: 'charset', charset: 'utf-8' },
      { hid: 'viewport', name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: OG_DESCRIPTION },
      { hid: 'author', name: 'author', content: 'Danes je nov dan' },
      { hid: 'og:image', property: 'og:image', content: OG_IMAGE },
      // { hid: 'og:image:width', property: 'og:image:width', content: '1200' },
      // { hid: 'og:image:height', property: 'og:image:height', content: '628' },
      { hid: 'og:title', property: 'og:title', content: OG_TITLE },
      { hid: 'og:description', property: 'og:description', content: OG_DESCRIPTION },
      // { hid: 'og:url', property: 'og:url', content: 'https://newsgradient.org/' },
      { hid: 'twitter:card', name: 'twitter:card', content: 'summary_large_image' },
      { hid: 'twitter:title', name: 'twitter:title', content: OG_TITLE },
      { hid: 'twitter:image', name: 'twitter:image', content: OG_IMAGE },
      { hid: 'twitter:description', name: 'twitter:description', content: OG_DESCRIPTION },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://use.typekit.net/rwb3jbn.css' },
    ],
    script: [
      {
        async: true,
        defer: true,
        'data-domain': 'newsgradient.org',
        src: 'https://plausible.lb.djnd.si/js/plausible.js',
      },
    ],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#e50001' },
  /*
   ** Global CSS
   */
  css: ['@/assets/style/main.scss'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxtjs/eslint-module',
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    // '@nuxtjs/pwa',
    'bootstrap-vue/nuxt',
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    proxy: false,
    baseURL: 'https://newsgradient-api.lb.djnd.si/',
    // baseURL: 'https://cors-anywhere.djnd.si/https://newsgradient-api.lb.djnd.si/',
    // baseURL: 'http://localhost:8000/'
    // baseUrl: process.env.API_BASE_URL || 'http://localhost:8000'
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {},
    postcss: {
      plugins: {
        autoprefixer: {},
      },
    },
  },
  /*
   ** Router configuration
   */
  // router: {
  // }
}
