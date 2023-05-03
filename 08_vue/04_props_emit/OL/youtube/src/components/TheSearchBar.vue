<template>
  <input type="text" v-model="inputData" @keyup.enter="SearchVideo">
</template>

<script>
export default {
    name:'TheSearchBar',
    data() {
        return {
            inputData: ''
        }
    },
    methods: {
        SearchVideo() {
            this.$emit('get-input', this.inputData)
        }
    }
}
</script>

<style>

</style>