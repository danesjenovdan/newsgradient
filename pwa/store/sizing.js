export const state = () => ({
  windowWidth: typeof window !== 'undefined' ? window.innerWidth : null,
})

export const mutations = {
  SET_WIDTH(state, payload) {
    state.windowWidth = payload
  },
}
