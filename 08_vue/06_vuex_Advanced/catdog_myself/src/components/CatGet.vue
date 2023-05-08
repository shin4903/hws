<template>
  <div style="display:flex; flex-wrap:wrap">
    <div v-for="cat in caturl" :key="cat" >
        <p class="color">cat</p>
        <img :src="cat" class="size">
    </div>
  </div>
</template>

<script>
export default {
    name : 'CatGet',
    computed : {
        caturl() {
        return this.$store.state.caturl
        },
        
    },
}
</script>

<style>
    .size {
        width: 300px;
        height: 300px;
    }
    .color{
        color: red;
        font-weight: bold;
    }
</style>