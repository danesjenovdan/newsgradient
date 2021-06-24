const OG_TITLE = 'Newsgradient BiH'
const OG_DESCRIPTION =
  'Pet najaktuelnijih vijesti u izvještajima bosanskohercegovačkih medija, poredanih po ideološkoj orijentaciji'
const OG_IMAGE = 'https://bih.newsgradient.org/newsgradient-og.png'

export default {
  mode: 'spa',
  /*
   ** Headers of the page
   */
  head: {
    title: OG_TITLE,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { name: 'description', content: OG_DESCRIPTION },
      { name: 'author', content: 'Danes je nov dan' },
      { property: 'og:image', content: OG_IMAGE },
      { property: 'og:image:width', content: '1200' },
      { property: 'og:image:height', content: '628' },
      { property: 'og:title', content: OG_TITLE },
      { property: 'og:description', content: OG_DESCRIPTION },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:title', content: OG_TITLE },
      { name: 'twitter:image', content: OG_IMAGE },
      { name: 'twitter:description', content: OG_DESCRIPTION }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://use.typekit.net/rwb3jbn.css' }
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
    '@nuxtjs/eslint-module'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    'bootstrap-vue/nuxt'
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    proxy: false,
    baseURL: 'https://newsgradient-api.lb.djnd.si/'
    // baseUrl: process.env.API_BASE_URL || 'http://localhost:8000'
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {}
  },
  /*
   ** Router configuration
   */
  // router: {
  // }
}
