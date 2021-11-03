<template>
  <div class="container--fluid flex flex-align--center flex-justify--center flex--column">
    <Header />
    <template v-if="aBlogPostLoaded">
      <div class="container--fluid">
        <div v-if="!isMobile" class="text-center">
          <h1 class="blog-title">{{ blogPost.title }}</h1>
          <p class="text--italic">{{ formatDate(blogPost.date) }}</p>
        </div>
      </div>
      <Divider v-if="!isMobile" class="w-100" />
      <div class="container">
        <b-row>
          <div class="col-12 my-4 blog-content">
            <!-- eslint-disable-next-line vue/no-v-html -->
            <div class="blog-text m-5" v-html="blogPost.text"></div>
          </div>
        </b-row>
      </div>
    </template>
    <template v-else>
      <animated-loader />
    </template>
  </div>
</template>

<script>
import Header from '../../components/Header'
import Divider from '../../components/Divider'
import AnimatedLoader from '../../components/AnimatedLoader'

export default {
  components: {
    Header,
    Divider,
    AnimatedLoader,
  },
  async asyncData({ store, route }) {
    await store.dispatch('blog/getABlogPost', { blogPostId: route.params.id })
  },
  computed: {
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
    blogPost() {
      return this.$store.state.blog.aBlogPost
    },
    aBlogPostLoaded() {
      return this.$store.state.blog.aBlogPostLoaded
    },
  },
  methods: {
    formatDate(value) {
      const d = new Date(value)
      return `${d.getDate()}.${d.getMonth() + 1}.${d.getFullYear()}`
    },
  },
  head() {
    return {
      title: this.blogPost.title,
      meta: [
        { hid: 'og:title', property: 'og:title', content: `${this.blogPost.title} - Newsgradient` },
        { hid: 'twitter:title', name: 'twitter:title', content: `${this.blogPost.title} - Newsgradient` },
        { hid: 'og:description', property: 'og:description', content: this.blogPost.short_description },
        { hid: 'twitter:description', name: 'twitter:description', content: this.blogPost.short_description },
        { hid: 'og:image', property: 'og:image', content: this.blogPost.image },
        { hid: 'twitter:image', name: 'twitter:image', content: this.blogPost.image },
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
.blog-title {
  text-align: center;
  font-style: italic;
  margin: 36px 0 25px 0;
  font-weight: 900;
  font-size: 36px;
  color: #3f3942;
  max-width: 60vw;
}

.blog-content {
  background-color: white;
}

.blog-text >>> p img {
  max-width: 100%;
}
.blog-text ::v-deep {
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-weight: 700;
  }
  img {
    max-width: 100%;
  }
}
</style>
