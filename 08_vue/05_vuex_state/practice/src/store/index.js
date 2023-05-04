import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    number : 0,
  },
  getters: {
    doubleNumber(state){
      return state.number * 2
    }
  },
  mutations: {
    UPNUMBER(state, payload) {
      state.number = payload + 1
    },
    DOWNNUMBER(state, payload) {
      state.number = payload - 1
    }
  },
  actions: {
    UpNumber(context, number) {
      context.commit('UPNUMBER', number)
    },
    DownNumber(context, number) {
      context.commit('DOWNNUMBER', number)
    }
  },
  modules: {
  }
})
