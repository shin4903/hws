import Vue from 'vue'
import Vuex from 'vuex'
// import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [
  //   createPersistedState(),
  // ],
  state: {
    caturl : [],
    dogurl : []
  },
  getters: {
  },
  mutations: {
    GET_CAT(state, url) {
      state.caturl.push(url)
    },
    GET_DOG(state, url) {
      state.dogurl.push(url)
    },
    LOAD_IMAGE(state) {
      const parseCat = JSON.parse(localStorage.getItem('caturl'))
      const parseDog = JSON.parse(localStorage.getItem('dogurl'))
      state.caturl = parseCat ? parseCat : []
      state.dogurl = parseDog ? parseDog : []
    }
  },
  actions: {
    getcat(context, url) {
      context.commit('GET_CAT', url)
      context.dispatch('saveGatUrl',url)
    },
    getdog(context, url) {
      context.commit('GET_DOG', url)
      context.dispatch('saveDogUrl',url)
    },
    saveGatUrl(context) {
      const url = JSON.stringify(context.state.caturl)
      localStorage.setItem('caturl', url)
    },
    saveDogUrl(context) {
      const url = JSON.stringify(context.state.dogurl)
      localStorage.setItem('dogurl', url)
    },
    loadImage(context) {
      context.commit('LOAD_IMAGE')
    }
  },
  modules: {
  }
})
