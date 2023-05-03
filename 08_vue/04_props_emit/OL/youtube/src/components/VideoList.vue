<template>
  <div>
    <VideoListItem 
    v-for="video in responseData"
    :key="video.id.videoId"
    :video="video.snippet.title"
    @get-video-data="SendVideo"/>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
    name:'VideoList',
    props: {
        responseData: Object
    },
    components: {
        VideoListItem
    },
    methods:{
        SendVideo(video) {
            this.$emit('get-video-title', video)
        }
    }
}
</script>

<style>

</style>