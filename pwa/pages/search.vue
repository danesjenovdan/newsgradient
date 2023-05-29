<template>
  <div class="container--fluid flex flex-align--center flex-justify--center flex--column">
    <Header />

    <div class="container my-4">
      <b-row>
        <div class="col-12 mb-4">
          <SearchBar :search-query="searchQuery" />
        </div>
      </b-row>

      <b-row>
        <div class="col-12">
          <SearchWrapper
            :title="`Rezultati za “${searchQuery}”`"
            :articles="allArticles"
            :article-count="allArticles.length"
            :all-articles-count="allArticles.length"
            :event-uri="''"
            :is-main="true"
            :first-publish="''"
            :social-score="0"
          />
        </div>
      </b-row>
    </div>
  </div>
</template>

<script>
import Header from '../components/Header'
import { API } from '../api'
import SearchWrapper from '../components/SearchWrapper'
import SearchBar from '../components/SearchBar.vue'

export default {
  components: {
    Header,
    SearchBar,
    SearchWrapper,
  },
  async asyncData({ $axios }) {
    const response = await $axios.get(API.news.newsletter)
    const events = response.data
    return { events }
  },
  data() {
    return {
      searchQuery: '',
      events: [],
    }
  },
  computed: {
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
    allArticles() {
      return this.events
        .map((e) => [...e.all_articles_slant_1, ...e.all_articles_slant_2, ...e.all_articles_slant_3])
        .flat()
    },
  },
  mounted() {
    this.searchQuery = this.$route.query.q || ''
  },
  methods: {},
}
</script>

<style lang="scss" scoped>
@import '@/assets/style/variables';

h1 {
  text-align: center;
  font-style: italic;
  margin: 36px 0 25px 0;
  font-weight: 900;
  font-size: 36px;
  color: #3f3942;
  max-width: 60vw;
}

h4 {
  font-style: italic;
  font-weight: 900;
  font-size: 24px;
  color: #3f3942;
}

.event-wrapper {
  margin-bottom: 40px;
}

.event {
  background-color: #fff;
  padding: 25px;
  height: 100%;
}
</style>
