<template>
  <div class="container--fluid flex flex-align--center flex-justify--center flex--column">
    <Header />
    <div class="container-landing">
      <div v-if="isMobile" class="description-container">
        Najaktuelnije vijesti u izvještajima bosanskohercegovačkih medija grupisane po ideološkoj orijentaciji.
      </div>
      <div class="row">
        <div class="col col-12 col-md-6 col-lg-8 mb30">
          <NewsletterBar />
        </div>
        <div class="col col-12 col-md-6 col-lg-4 mb30">
          <SearchBar />
        </div>
      </div>
      <div v-if="!isMobile" class="row flex flex--wrap">
        <div v-for="(event, index) in topEvents" :key="event.id" class="col-xl-8 col-12 mb30">
          <EventWrapper
            :title="event.title"
            :articles="event.articles"
            :article-count="event.articleCount"
            :all-articles-count="event.allArticlesCount"
            :event-uri="event.id"
            :is-main="index === 0"
            :first-publish="event.firstPublish"
            :social-score="event.social_score"
          />
        </div>
        <template v-for="event in otherEvents">
          <div :key="event.id" class="col-xl-4 col-lg-6 col-12 mb30">
            <EventWrapper
              :title="event.title"
              :articles="event.articles"
              :is-main="false"
              :event-uri="event.id"
              :article-count="event.articleCount"
              :all-articles-count="event.allArticlesCount"
              :first-publish="event.firstPublish"
              :social-score="event.social_score"
            />
          </div>
        </template>
      </div>
      <div v-else>
        <div v-for="ev in allEvents" :key="ev.title">
          <MobileEvent
            v-if="ev.articles.length"
            :title="ev.title"
            :image-url="ev.image"
            :first-publish="ev.firstPublish"
            :article-count="ev.articleCount"
            :all-articles-count="ev.allArticlesCount"
            :event-uri="ev.id"
            :social-score="ev.social_score"
          />
        </div>
      </div>
    </div>
    <div v-if="!isMobile">
      <SelectorNew @change="slantChanged" />
    </div>
  </div>
</template>

<script>
import EventWrapper from '../components/EventWrapper'
import SelectorNew from '../components/SelectorNew'
import MobileEvent from '../components/MobileEvent'
import Header from '../components/Header'
import NewsletterBar from '../components/NewsletterBar'
import SearchBar from '../components/SearchBar'

export default {
  components: {
    Header,
    MobileEvent,
    SelectorNew,
    EventWrapper,
    NewsletterBar,
    SearchBar,
  },
  async asyncData({ store, route }) {
    const slant = ['1', '2', '3'].includes(route.query.slant)
      ? Number(route.query.slant)
      : store.state.carousel.selectedSlant
    await store.dispatch('carousel/setSlant', slant)
    await store.dispatch('events/getTopEvents', { slant, timerange: store.state.events.timerange })
  },
  computed: {
    topEvents() {
      return this.$store.state.events.topEvents.slice(0, 1)
    },
    allEvents() {
      return this.$store.state.events.topEvents
    },
    otherEvents() {
      return this.$store.state.events.topEvents.slice(1)
    },
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
  },
  mounted() {
    this.updateSlantUrl()
  },
  methods: {
    slantChanged(slant) {
      this.$store.dispatch('carousel/setSlant', slant)
      this.$store.dispatch('events/getTopEvents', { slant, timerange: this.$store.state.events.timerange })
      this.updateSlantUrl()
    },
    updateSlantUrl() {
      const slant = this.$store.state.carousel.selectedSlant
      const url = new URL(window.location)
      if (!url.searchParams.has('slant') || url.searchParams.get('slant') !== String(slant)) {
        url.searchParams.set('slant', slant)
        window.history.replaceState(null, '', `${url.pathname}${url.search}`)
      }
    },
  },
}
</script>

<style scoped lang="scss">
@import '@/assets/style/variables';

.container-landing {
  width: 90%;
  margin-bottom: 100px;
  margin-top: 80px;

  @media (max-width: $medium) {
    margin-top: 0;
    margin-bottom: 80px;
    width: auto;
    padding: 0 8px;
  }
}
.large-container {
  width: 66%;
}

.small-container {
  width: 33%;
}

.timing-container {
  display: none;
  @media (min-width: $medium) {
    display: block;
  }
}

.description-container {
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
  line-height: 1.1;

  @media (max-width: $medium) {
    max-width: 250px;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
