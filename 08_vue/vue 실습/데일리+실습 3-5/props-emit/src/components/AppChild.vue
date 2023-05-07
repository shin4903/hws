<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" v-model="childData" @input="ChildToParents">
    <p>appData : {{appData}}</p>
    <p>parentData : {{parentData}}</p>
  </div>
</template>

<script>
export default {
  name : "AppChild",
  props: {
    appData : String,
    parentData: String
  },
  data() {
    return {
      childData: null
    }
  },
  methods: {
    ChildToParents() {
      this.$emit('child-to-parent',this.childData)
    },
  }
}
</script>

<style>

</style>