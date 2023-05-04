<template>
  <div id="app">
    <p>Counter : {{number}}</p>
    <p>Counterx2 : {{doubleNumber}}</p>
    <button @click="increase">increase</button>
    <button @click="decrease">decrease</button>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {

  },
  computed: {
    number() {
      return this.$store.state.number
    },
    doubleNumber() {
      return this.$store.getters.doubleNumber
    }
    
  },
  methods: {
    increase(){
      const NewNumber = this.number
      this.$store.dispatch('UpNumber', NewNumber)
    },
    decrease() {
      const NewNumber = this.number
      this.$store.dispatch('DownNumber', NewNumber)
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
