<template>
  <div class="container--fluid flex flex-align--center flex-justify--center flex--column">
    <Header />
    <div class="container--fluid">
      <div v-if="!isMobile" class="flex flex-align--center flex-justify--center">
        <h1 class="blog-title">{{ blogPost.title }}</h1>
      </div>
    </div>
    <Divider v-if="!isMobile" class="w-100" />
    <div class="container">
      <b-row>
        <div class="col-12 my-4 blog-content">
          <div v-html="blogPost.text" class="m-4"></div>
        </div>
      </b-row>
    </div>
  </div>
</template>

<script>
import Header from '../../components/Header'
import Divider from '../../components/Divider'

export default {
  components: {
    Header,
    Divider,
  },
  computed: {
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
    blogPost() {
      return this.$store.state.blog.aBlogPost
    },
  },
  mounted() {
    this.getABlogPost()
  },
  methods: {
    getABlogPost() {
      this.$store.dispatch('blog/getABlogPost', { blogPostId: this.$route.params.id })
    },
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
  p img {
    max-width: 100%;
  }
}
img {
  max-width: 100%;
}
</style>
