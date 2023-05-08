import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    images : [],
    // 사용자가 select를 바꿀 때 마다 바뀌어야 함
    status : 'all'
  },
  // computed와 같은 역할을 해준다
  getters: {
    // 사용자가 선택한 status에 따라서 반환해줄 배열의 내용물을 바꾼다.
    // all이라면 모든 이미지를
    // cat이면 고양이 이미지
    // dog이면 개 이미지만 
    getStatusByImages(state) {
      const images = state.images.filter(image => {
        if (state.status === 'dog') {
          return image.status === 'dog'
        } else if (state.status ==='cat') {
          return image.status === 'cat'
        } else {
          return image
        }
      })
      return images
    }
  },
  mutations: {
    GET_IMAGE(state, payload) {
      // 상태 변화
      state.images.push(payload)
    },
    CHANGE_STAUTS(state, payload){
      state.status = payload
    }
  },
  actions: {
    // actions에 정의하는 메서드는 인자로 context를 첫번째로 넘겨 받는다
    // context를 통해서 다른 객체나 속성에 접근할 일 없이 commit (mutations를 호출만 헐거라면)
    // conts commit = context.commit
    // const {commit} = context
    getCatImage({commit}) {
      axios({
        method : 'get',
        url : 'https://api.thecatapi.com/v1/images/search'
      })
      .then(res => {
        // state에 저장 될 데이터 전처리
        const payload = {
          id : new Date().getTime(),
          url : res.data[0].url,
          status: 'cat'
        }
        commit('GET_IMAGE',payload)
      })
      .catch(err => console.log(err))

    },
    getDogImage({commit}) {
      axios({
        method : 'get',
        url : 'https://dog.ceo/api/breeds/image/random'
      })
      .then(res => {
        // state에 저장 될 데이터 전처리
        const payload = {
          id : new Date().getTime(),
          url : res.data.message,
          status: 'dog'
        }
        commit('GET_IMAGE',payload)
      })
      .catch(err => console.log(err))
    },

    changeStatus({commit}, payload) {
      commit('CHANGE_STAUTS', payload)
    }
    
  },
  modules: {
  }
})
