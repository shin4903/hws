<template>
  <div>
    <p v-if="!imgSrc">{{message}}</p>
    <img v-if="imgSrc" :src="imgSrc" >
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name : 'DogView',
    data() {
        return {
            imgSrc: null,
            message: '로딩중.....'
        }
    },
    methods: {
        getDogImage() {
            const breed = this.$route.params.breed
            const dogImageSearchUrl = `https://dog.ceo/api/breed/${breed}/images/random`

            axios({
                method: 'get',
                url : dogImageSearchUrl
            })
            .then(res => {
                this.imgSrc = res.data.message
            })
            .catch(() => { 
                // this.message = `${this.$route.params.breed}는 없는 품종입니다.`
                this.$router.push('/404')
            })
        }
    },
    created() {
        this.getDogImage()
    }
}
</script>

<style>

</style>