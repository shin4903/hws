import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedstate from 'vuex-persistedstate'
import router from '@/router'
const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedstate()
  ],
  state: {
    articles: [
    ],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },

    // signup & login -> 완료하면 토큰 발급 -> 
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $rouer 접근 불가 -> import를 해야함
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },

    signUp(context,payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method : 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {username, password1, password2}
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err => console.log(err))
    },

    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then(res => {
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
