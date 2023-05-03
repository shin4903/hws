<template>
  <div id="app">
    <h1>My first youtube project</h1>
    <TheSearchBar @get-input="SearchVideo"/>
    <VideoList
    :response-data="responseData"
    @get-video-title="GoDetail"
    />
  </div>
</template>

<script>
import TheSearchBar from './components/TheSearchBar.vue'
import axios from 'axios'
import VideoList from './components/VideoList.vue'


export default {
  name: 'App',
  data () {
    return {
      responseData : {}
    }
  },
  components: {
    TheSearchBar,
    VideoList,
  },
  methods: {
    SearchVideo(inputData) {
     axios.get(
      'https://www.googleapis.com/youtube/v3/search/',
      {params: {part:'snippet', type: 'video', key:'AIzaSyCUnmub-IzzHxmx_-SDA9iok9yxbKURfp4', q:`${inputData}`}}
     )
     .then(response => {
      this.responseData = response.data.items
     })
    },
    GoDetail
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
