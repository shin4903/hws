<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>parentData : {{parentData}}</p>
    <p>childData : {{childData}}</p>
    <AppParent :app-data="appData" @child-to-app="ChildToApp" @parent-to-app="ParentToApp"/>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent
  },
  data () {
    return {
      appData : null,
      childData : null,
      parentData : null
    }
  },
  methods: {
    ChildToApp(childData) {
      this.childData = childData
    },
    ParentToApp(parentData) {
      this.parentData = parentData
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
