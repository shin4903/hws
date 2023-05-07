<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" v-model="parentData" @input="ParentToApp">
    <p>appData : {{appData}}</p>
    <p>childData : {{childData}}</p>
    <AppChild :app-data="appData" @child-to-parent="ChildToParents" :parent-data="parentData"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'

export default {
  name : "AppParent",
  components: {
    AppChild
  },
  props: {
    appData:String
  },
  data () {
    return {
      parentData : null,
      childData : null
    }
  },
  methods: {
    ChildToParents(childData) {
      this.childData = childData
      this.$emit('child-to-app', childData)
    },
    ParentToApp() {
      this.$emit('parent-to-app', this.parentData)
    }
  }
}
</script>

<style>

</style>