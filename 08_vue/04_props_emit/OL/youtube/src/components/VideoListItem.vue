<template>
  <div> 
    <p @click="announce(video)">{{video}}</p><br>
  </div>
</template>

<script>
export default {
    name:'VideoListItem',
    // data () {
    //     return {
    //         videoData: ''
    //     }
    // },
    props: {
        video: String
    },
    methods: {
        announce(video){
            this.$emit('get-video-data', video)
        }
    }
}
</script>

<style>

</style>