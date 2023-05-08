<template>
  <div style="display:flex; flex-wrap:wrap">
    <div v-for="dog in dogurl" :key="dog" >
        <p class="color1">dog</p>
        <img :src="dog" class="size">
    </div>

  </div>
</template>

<script>
export default {
    name : 'DogGet',
    computed : {
        dogurl() {
            return this.$store.state.dogurl
        }
    },

}
</script>

<style>
    .size {
            width: 300px;
            height: 300px;
        }
    
    .color1{
        color: blue;
        font-weight: bold;
    }
</style>