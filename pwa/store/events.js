import { API } from '../api'
import { TIMERANGE } from '../constants'

export const state = () => ({
  topEvents: [],
  articles: {},
  timerange: TIMERANGE.TODAY,
  eventTitle: '',
  eventDescription: '',
  eventImage: '',
  locations: [],
  positive: [],
  slightlyPositive: [],
  neutral: [],
  slightlyNegative: [],
  negative: [],
})

export const mutations = {
  SET_TOP_EVENTS(state, payload) {
    state.topEvents = payload
  },
  SET_ARTICLES(state, payload) {
    state.articles = payload
  },
  SET_TIMERANGE(state, payload) {
    state.timerange = payload
  },
  SET_EVENT_TITLE(state, payload) {
    state.eventTitle = payload
  },
  SET_EVENT_DESCRIPTION(state, payload) {
    state.eventDescription = payload
  },
  SET_EVENT_IMAGE(state, payload) {
    state.eventImage = payload
  },
  SET_LOCATIONS(state, payload) {
    state.locations = payload
  },
  SET_POSITIVE_PARTIES(state, payload) {
    state.positive = payload
  },
  SET_SLIGHTLY_POSITIVE_PARTIES(state, payload) {
    state.slightlyPositive = payload
  },
  SET_NEUTRAL_PARTIES(state, payload) {
    state.neutral = payload
  },
  SET_SLIGHTLY_NEGATIVE_PARTIES(state, payload) {
    state.slightlyNegative = payload
  },
  SET_NEGATIVE_PARTIES(state, payload) {
    state.negative = payload
  },
}

export const actions = {
  // async getTopEvents(context, payload = {}) {
  //   try {
  //     let url = API.news.topEvents
  //     const qp = {}
  //     if (payload.slant) {
  //       qp.slant = payload.slant
  //     }
  //     const params = new URLSearchParams(qp).toString()
  //     if (params) {
  //       url += '?' + params
  //     }

  //     const response = await this.$axios.get(url)
  //     context.commit('SET_TOP_EVENTS', response.data)
  //   } catch (e) {}
  // },
  async getTopFilteredEvents(context, payload = {}) {
    try {
      let url = API.news.topFilteredEvents
      const qp = {}
      if (payload.locations) {
        qp.locations = payload.locations.join(',')
      }
      if (payload.positive) {
        qp.positive = payload.positive.join(',')
      }
      if (payload.slightlyPositive) {
        qp.slightly_positive = payload.slightlyPositive.join(',')
      }
      if (payload.neutral) {
        qp.neutral = payload.neutral.join(',')
      }
      if (payload.slightlyNegative) {
        qp.slightly_negative = payload.slightlyNegative.join(',')
      }
      if (payload.negative) {
        qp.negative = payload.negative.join(',')
      }
      const params = new URLSearchParams(qp).toString()
      if (params) {
        url += '?' + params
      }

      const response = await this.$axios.get(url)
      context.commit('SET_TOP_EVENTS', response.data)
    } catch (e) {}
  },
  // async getEventArticles(context, { eventId }) {
  //   try {
  //     // debugger
  //     const url = API.news.articles + eventId + '/'
  //     const response = await this.$axios.get(url)
  //     const data = response.data
  //     const result = {
  //       1: [],
  //       2: [],
  //       3: [],
  //       4: [],
  //       5: [],
  //     }
  //     data.articles.forEach((article) => {
  //       result[parseInt(article.medium.slant)].push(article)
  //     })
  //     context.commit('SET_ARTICLES', result)
  //     context.commit('SET_EVENT_TITLE', data.title)
  //     context.commit('SET_EVENT_DESCRIPTION', data.description)
  //     context.commit('SET_EVENT_IMAGE', data.og_image)
  //   } catch (e) {}
  // },
  async getEventFilteredArticles(context, payload = {}) {
    try {
      let url = API.news.filteredArticles + payload.eventId + '/'
      const qp = {}
      if (payload.locations) {
        qp.locations = payload.locations.join(',')
      }
      if (payload.positive) {
        qp.positive = payload.positive.join(',')
      }
      if (payload.slightlyPositive) {
        qp.slightly_positive = payload.slightlyPositive.join(',')
      }
      if (payload.neutral) {
        qp.neutral = payload.neutral.join(',')
      }
      if (payload.slightlyNegative) {
        qp.slightly_negative = payload.slightlyNegative.join(',')
      }
      if (payload.negative) {
        qp.negative = payload.negative.join(',')
      }
      const params = new URLSearchParams(qp).toString()
      if (params) {
        url += '?' + params
      }

      const response = await this.$axios.get(url)
      const data = response.data
      context.commit('SET_ARTICLES', data.articles)
      context.commit('SET_EVENT_TITLE', data.title)
      context.commit('SET_EVENT_DESCRIPTION', data.description)
      context.commit('SET_EVENT_IMAGE', data.og_image)
    } catch (e) {}
  },
  setTimerange(context, payload) {
    context.commit('SET_TIMERANGE', payload)
  },
  setLocations(context, payload) {
    context.commit('SET_LOCATIONS', payload)
  },
  setPositiveParties(context, payload) {
    context.commit('SET_POSITIVE_PARTIES', payload)
  },
  setSlightlyPositiveParties(context, payload) {
    context.commit('SET_SLIGHTLY_POSITIVE_PARTIES', payload)
  },
  setNeutralParties(context, payload) {
    context.commit('SET_NEUTRAL_PARTIES', payload)
  },
  setSlightlyNegativeParties(context, payload) {
    context.commit('SET_SLIGHTLY_NEGATIVE_PARTIES', payload)
  },
  setNegativeParties(context, payload) {
    context.commit('SET_NEGATIVE_PARTIES', payload)
  },
}
