<template>
  <div class="container--fluid flex flex-align--center flex-justify--center flex--column">
    <Header />
    <div class="container--fluid">
      <div v-if="!isMobile" class="flex flex-align--center flex-justify--center">
        <h1>Blog</h1>
      </div>
    </div>
    <Divider v-if="!isMobile" class="w-100" />
    <div class="container">
      <b-row v-if="blogPostsLoaded" class="my-4">
        <div v-for="(bp, i) in blogPosts" :key="i" class="col-lg-4 col-md-6 article-card-wrapper">
          <div class="event-article-preview">
            <div class="image-ratio">
              <!--              <div :style="{ backgroundImage: `url(${fixedImageUrl}), url(/missing-image.png)` }" class="article-image"></div>-->
              <div :style="{ backgroundImage: `url(${bp.image}), url(/missing-image.png)` }" class="article-image"></div>
            </div>
            <div class="article-info">
              <div class="text--italic pb-2">{{ formatDate(bp.date) }}</div>
              <div class="article-content">
                <span class="article-title">{{ bp.title }} /</span>
                <span class="article-description">
                  {{ bp.short_description }}
                </span>
                <div>
                  <a :href="`blog/${bp.id}/`" class="read-more stretched-link"> Pročitaj više </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </b-row>
      <b-row v-else class="justify-content-center">
        <animated-loader />
      </b-row>
      <b-row v-if="blogPostsLoaded && blogPosts && count > 1">
        <b-col cols="12">
          <Pagination :page="page" @select-page="selectPage" />
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import Header from '../../components/Header'
import Divider from '../../components/Divider'
import Pagination from '../../components/Pagination'
import AnimatedLoader from '../../components/AnimatedLoader'

export default {
  components: {
    Pagination,
    Header,
    Divider,
    AnimatedLoader,
  },
  data() {
    return {
      page: 1,
    }
  },
  computed: {
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
    blogPosts() {
      return this.$store.state.blog.blogPosts
    },
    blogPostsLoaded() {
      return this.$store.state.blog.blogPostsLoaded
    },
    count() {
      return this.$store.state.blog.pageCount
    },
  },
  mounted() {
    if (this.$route.query.page) {
      const page = parseInt(this.$route.query.page)
      if (Number.isInteger(page) && page > 0) {
        this.page = page
      }
    }
    this.getBlogPosts()
  },
  methods: {
    getBlogPosts() {
      this.$store.dispatch('blog/getBlogPosts', { page: this.page })
    },
    selectPage(value) {
      this.page = value
      this.$router.push({ path: '', query: { page: value } })
      this.getBlogPosts()
    },
    formatDate(value) {
      const d = new Date(value)
      return `${d.getDate()}.${d.getMonth() + 1}.${d.getFullYear()}`
    },
  },
}
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
  font-style: italic;
  margin: 36px 0 25px 0;
  font-weight: 900;
  font-size: 36px;
  color: #3f3942;
  max-width: 60vw;
}

.article-card-wrapper {
  margin-bottom: 16px;
  padding-right: 8px;
  padding-left: 8px;
}
.event-article-preview {
  border: 1px solid #a8a5a9;
  width: 100%;
  height: 100%;
  margin-bottom: 10px;
  margin-left: 5px;
  margin-right: 5px;
  background-color: #f6f6f6;
  transition: background-color 0.15s ease-in-out;
  position: relative;

  &:first-child {
    margin-left: 0;
  }

  &:last-child {
    margin-right: 0;
  }

  &:hover {
    background-color: #fdfdfd;
  }

  .image-ratio {
    .article-image {
      height: 0;
      padding-top: 56.25%;
      background-position: center center;
      background-size: cover;
      position: relative;
    }
  }

  .article-medium {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 18px;

    .medium-brand {
      flex-shrink: 0;
      display: flex;
      align-items: center;

      .favicon {
        width: 26px;
        height: 26px;
        background-color: #ededed;
      }

      .medium-name {
        margin-left: 0.5rem;
        color: #000;
        font-size: 1rem;
        font-style: italic;
        line-height: 1.25rem;
      }
    }

    .medium-link {
      flex-shrink: 0;
      font-size: 0.65rem;
      color: #07f;
      line-height: 1.25rem;
      margin-left: auto;
      display: inline;
      vertical-align: middle;

      &:hover {
        text-decoration: none;
      }
    }

    .social-score-badge {
      display: flex;
      align-items: center;
      background-color: white;
      border-radius: 5em;
      padding: 4px 6px;
      font-size: 12px;
      font-weight: 400;

      .icon {
        display: inline-block;
        margin-left: 4px;
        width: 14px;
        height: 14px;
        background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="%23000" d="M18.9 7c.8-.5 1.3-1.2 1.6-2-.8.4-1.6.7-2.4.9-.7-.8-1.6-1.1-2.7-1.1-1 0-1.9.4-2.6 1.1a3.63 3.63 0 00-1 3.4c-3-.2-5.5-1.5-7.5-3.9-.4.6-.6 1.2-.6 1.8 0 1.3.5 2.3 1.6 3.1-.6-.1-1.2-.2-1.6-.5 0 .9.3 1.7.8 2.4s1.3 1.1 2.1 1.3c-.3.1-.6.1-1 .1-.3 0-.5 0-.7-.1.2.8.7 1.4 1.3 1.8.6.5 1.3.7 2.2.7-1.3 1-2.9 1.6-4.6 1.6h-.9c1.7 1.1 3.6 1.6 5.7 1.6a10.23 10.23 0 009.3-5.6c.8-1.6 1.2-3.2 1.2-4.9v-.4c.8-.6 1.4-1.2 1.8-1.9-.6.3-1.3.5-2 .6z"/></svg>');
      }
    }
  }

  .tags {
    margin: 0.75rem 0 0.5rem;

    .tag {
      display: inline-block;
      font-size: 0.75rem;
      background-color: #07f;
      color: #fff;
      padding: 0.25rem 0.5rem;
    }
  }

  .article-info {
    padding: 15px 21px;

    .article-content {
      display: block;
      line-height: 1;

      .article-title {
        display: inline;
        margin: 0;
        font-size: 20px;
        font-weight: 700;
        color: #3f3942;
        line-height: 1.1;
        word-break: break-word;
      }

      .article-description {
        display: inline;
        line-height: 1.3;
        word-break: break-word;
      }

      .read-more {
        display: inline-block;
        color: #07f;
        text-decoration: underline;
        line-height: 1.3;
      }
    }
  }
}
</style>
