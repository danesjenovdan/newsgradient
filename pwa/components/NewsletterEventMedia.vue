<template>
  <div class="text-center">
    <div>
      <div class="article-url">
        <a v-for="article in articles" :key="article.title" :href="`${article.url}`">
          <img :src="`${faviconIcon(article.url)}`" :title="`${article.medium__title}`" />
        </a>
      </div>
    </div>
    <div class="media-article-text">{{ articles.length }} {{ articlesText }}</div>
    <div class="media-slant-text">
      {{ mediaSlantText }}
    </div>
  </div>
</template>

<script>
import { faviconIcon } from '../utils'

export default {
  props: {
    articles: {
      type: Array,
      required: true,
    },
    mediaSlantText: {
      type: String,
      required: true,
    },
  },
  data() {
    return {}
  },
  computed: {
    articlesText() {
      return this.articles.length > 1 ? 'članaka' : 'članak'
    },
  },
  methods: {
    faviconIcon(url) {
      return faviconIcon(url)
    },
  },
}
</script>

<style scoped>
.article-url {
  max-width: 90px;
  margin: 0 auto;
}
.article-url a {
  display: inline-block;
  text-decoration: none;
}
.article-url a img {
  display: inline-block;
  width: 16px;
  height: 16px;
}
.media-article-text {
  color: #222;
  font-size: 16px;
  font-weight: 700;
  line-height: 1.2;
}
.media-slant-text {
  color: #222;
  font-size: 11px;
  font-weight: 600;
}
</style>
