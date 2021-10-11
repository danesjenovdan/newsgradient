import { API } from '../api'

export const state = () => ({
  blogPosts: [],
  aBlogPost: {},
  pageCount: 1,
})

export const mutations = {
  SET_BLOG_POSTS(state, payload) {
    state.blogPosts = payload
  },
  SET_PAGE_COUNT(state, payload) {
    state.pageCount = payload
  },
  SET_A_BLOG_POST(state, payload) {
    state.aBlogPost = payload
  },
}

export const actions = {
  async getBlogPosts(context, payload) {
    try {
      const url = API.blog.blogPosts + '?page=' + payload.page
      // const qp = {}
      /*
      const params = new URLSearchParams(qp).toString()
      if (params) {
        url += '?' + params
      }
      */
      const response = await this.$axios.get(url)
      context.commit('SET_BLOG_POSTS', response.data.results)
      const pageCount = Math.ceil(parseInt(response.data.count) / 9)
      context.commit('SET_PAGE_COUNT', pageCount)
    } catch (e) {
      console.log(e)
    }
  },
  async getABlogPost(context, { blogPostId }) {
    try {
      const url = API.blog.blogPosts + blogPostId + '/'
      const response = await this.$axios.get(url)
      const data = response.data
      context.commit('SET_A_BLOG_POST', data)
    } catch (e) {
      console.log(e)
    }
  },
}
