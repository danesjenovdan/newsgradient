import { API } from '../api'
import { TIMERANGE } from '../constants'

export const state = () => ({
  topEvents: [],
  articles: {},
  timerange: TIMERANGE.TODAY,
  eventTitle: '',
  eventDescription: '',
  eventImage: '',
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
}

export const actions = {
  async getTopEvents(context, payload = {}) {
    try {
      let url = API.news.topEvents
      const qp = {}
      if (payload.slant) {
        qp.slant = payload.slant
      }
      const params = new URLSearchParams(qp).toString()
      if (params) {
        url += '?' + params
      }

      const response = await this.$axios.get(url)
      context.commit('SET_TOP_EVENTS', response.data)
    } catch (e) {}
  },
  async getEventArticles(context, { eventId }) {
    try {
      // debugger
      const url = API.news.articles + eventId + '/'
      const response = await this.$axios.get(url)
      const data = response.data
      const result = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
      }
      data.articles.forEach((article) => {
        result[parseInt(article.medium.slant)].push(article)
      })
      context.commit('SET_ARTICLES', result)
      context.commit('SET_EVENT_TITLE', data.title)
      context.commit('SET_EVENT_DESCRIPTION', data.description)
      context.commit('SET_EVENT_IMAGE', data.og_image)
    } catch (e) {}
  },
  setTimerange(context, payload) {
    context.commit('SET_TIMERANGE', payload)
  },
}
