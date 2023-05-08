<template>
  <div id="app">
    <button @click="getcat">cat</button>
    <button @click="getdog">dog</button>
    <hr>
    <CatGet/>
    <DogGet/>
  </div>
</template>

<script>
import axios from 'axios'
import CatGet from './components/CatGet.vue'
import DogGet from './components/DogGet.vue'

export default {
  name: 'App',
  components: {
    CatGet,
    DogGet
  },
  created() {
    this.$store.dispatch('loadImage')
  },
  computed : {
    caturl() {
      return this.$store.state.caturl
    },
    dogurl() {
      return this.$store.state.dogurl
    }
  },
  methods: {
    getcat() {
      axios({
        method : 'get',
        url : 'https://api.thecatapi.com/v1/images/search'
      })
      .then(res => {
        this.$store.dispatch('getcat', res.data[0].url)
      })
    },
    getdog() {
      axios({
        method : 'get',
        url : 'https://dog.ceo/api/breeds/image/random'
      })
      .then(res => {
        this.$store.dispatch('getdog', res.data.message)
      })
    }
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
