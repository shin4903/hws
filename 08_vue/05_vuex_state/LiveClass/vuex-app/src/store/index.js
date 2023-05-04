import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
  getters: {
    messageLength(state) {
      return state.message.length
    },
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }

  },
  mutations: {
    CHANGE_MESSAGE(state, payload)  { // payload는 actions에서 넘겨준 message
      state.message = payload
    }
         
  },
  actions: {
    changeMessage(context, message) { //message는 Vue에서 넘겨준 newMessage 
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
