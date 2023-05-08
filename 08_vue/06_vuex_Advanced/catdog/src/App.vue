<template>
  <div id="app">
    <!-- 클릭했을 때 AJAX 요청을 보내도록 해야한다. -->
    <!-- ~하면 ~한다. envent에 대한 일을 처리 -->
    <!-- 1. @click => method를 실행한다. -->
    <button @click="getCatImage">getCat</button>
    <!-- 위쪽은 vue instance의 method를 호출 -->
    <!-- 아랫쪽은 store의 actions에 정의한 getDogImage호출 -->
    <button @click="getDogImage">getDog</button>
    <hr>
  <AnimalImages/>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import AnimalImages from './components/AnimalImages.vue'

// 현재 컴포넌트의 Vue instance의 method를 실행 -> methods들을 정의하고, 대상을 호출
export default {
  name: 'App',
  components: {
    AnimalImages
  },
  methods : {
    getCatImage() {
      // actions에서 axios 요청을 보낼 method 정의
      // actions에 정의한 getCatImage를 호출한다.
      this.$store.dispatch('getCatImage')
    },
    // getDogImage() {
      //   this.$store.dispatch('getDogImage')
    // }
      ...mapActions(['getDogImage']),
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
