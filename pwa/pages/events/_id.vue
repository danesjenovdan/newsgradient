<template>
  <div>
    <div class="container--fluid">
      <SubHeader v-if="isMobile">
        <div class="flex flex-align--center">
          <div class="flex--1">
            <img
              src="@/assets/svg/carousel/right-arrow.svg"
              class="back-button back-button--header"
              @click="$router.push('/')"
            />
          </div>
          <div class="flex--5 text--center header--title">{{ $store.state.events.eventTitle }}</div>
          <div class="flex--1"></div>
        </div>
      </SubHeader>
      <Header v-else />
      <div v-if="!isMobile" class="flex flex-align--center flex-justify--center">
        <h1>
          {{ $store.state.events.eventTitle }}
        </h1>
      </div>
      <Divider v-if="!isMobile" />
    </div>
    <div class="mt24">
      <Carousell :is-mobile="isMobile" @change="slantChanged" />
    </div>
    <b-row>
      <b-col>
        <SelectorNew @changeLocations="locationsChanged" @changeParties="partiesChanged" />
      </b-col>
    </b-row>
  </div>
</template>

<script>
import SelectorNew from '../../components/SelectorNew'
import Carousell from '../../components/Carousell'
import SubHeader from '../../components/SubHeader'
import Header from '../../components/Header'
import Divider from '../../components/Divider'

export default {
  components: {
    Divider,
    Header,
    SubHeader,
    Carousell,
    SelectorNew,
  },
  async asyncData({ store, route }) {
    // const slant = ['1', '2', '3'].includes(route.query.slant)
    //   ? Number(route.query.slant)
    //   : store.state.carousel.selectedSlant
    // await store.dispatch('carousel/setSlant', slant)
    await store.dispatch('events/getEventFilteredArticles', {
      eventId: route.params.id,
      // slant,
      locations: store.state.events.locations,
      positive: store.state.events.positive,
      slightlyPositive: store.state.events.slightlyPositive,
      neutral: store.state.events.neutral,
      slightlyNegative: store.state.events.slightlyNegative,
      negative: store.state.events.negative,
      // timerange: store.state.events.timerange,
    })
  },
  head() {
    const title = this.$store.state.events.eventTitle
    const description = this.$store.state.events.eventDescription
    const image = this.$store.state.events.eventImage || this.$store.state.events.articles?.[0]?.image
    return {
      title,
      meta: [
        { hid: 'og:title', property: 'og:title', content: `${title} - Newsgradient` },
        { hid: 'twitter:title', name: 'twitter:title', content: `${title} - Newsgradient` },
        { hid: 'og:description', property: 'og:description', content: description },
        { hid: 'twitter:description', name: 'twitter:description', content: description },
        { hid: 'og:image', property: 'og:image', content: image },
        { hid: 'twitter:image', name: 'twitter:image', content: image },
      ],
    }
  },
  computed: {
    isMobile() {
      return this.$store.state.sizing.windowWidth <= 768
    },
  },
  mounted() {
    // this.updateSlantUrl()
  },
  methods: {
    locationsChanged(locations) {
      this.$store.dispatch(
        'events/setLocations',
        locations.map((t) => t.name)
      )

      this.slantChanged()
    },
    partiesChanged(parties) {
      const positive = parties.filter((p) => p.slant === 5).map((p) => p.id)
      const slightlyPositive = parties.filter((p) => p.slant === 4).map((p) => p.id)
      const neutral = parties.filter((p) => p.slant === 3).map((p) => p.id)
      const slightlyNegative = parties.filter((p) => p.slant === 2).map((p) => p.id)
      const negative = parties.filter((p) => p.slant === 1).map((p) => p.id)
      this.$store.dispatch('events/setPositiveParties', positive)
      this.$store.dispatch('events/setSlightlyPositiveParties', slightlyPositive)
      this.$store.dispatch('events/setNeutralParties', neutral)
      this.$store.dispatch('events/setSlightlyNegativeParties', slightlyNegative)
      this.$store.dispatch('events/setNegativeParties', negative)

      this.slantChanged()
    },
    slantChanged(slant) {
      // this.$store.dispatch('carousel/setSlant', slant)
      this.$store.dispatch('events/getEventFilteredArticles', {
        eventId: this.$route.params.id,
        // slant,
        locations: this.$store.state.events.locations,
        positive: this.$store.state.events.positive,
        slightlyPositive: this.$store.state.events.slightlyPositive,
        neutral: this.$store.state.events.neutral,
        slightlyNegative: this.$store.state.events.slightlyNegative,
        negative: this.$store.state.events.negative,
        // timerange: this.$store.state.events.timerange,
      })

      // this.updateSlantUrl()
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

<style lang="scss">
@import '@/assets/style/variables';

.section-title {
  text-align: center;
  margin: 1.5rem 0;
  font-size: 40px;
  font-weight: 400;
  line-height: 35px;

  @media (max-width: $medium) {
    font-size: 1.5rem;
    line-height: unset;
  }
}
.section-line {
  height: 5px;
  width: 100vw;
  background-image: linear-gradient(to right, #0076fe 0%, #e50001 100%);
}

.content-wrapper {
  margin-bottom: 5vh;
}

h1 {
  text-align: center;
  font-style: italic;
  margin: 36px 0 25px 0;
  font-weight: 900;
  font-size: 36px;
  color: #3f3942;
  max-width: 60vw;
}
</style>
