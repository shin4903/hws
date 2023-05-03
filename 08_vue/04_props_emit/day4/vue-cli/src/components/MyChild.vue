<template>
  <div>
    <h3>This is child component</h3>
    <p>{{ staticProps }}</p>
    <p>{{ myProps }}</p>
    <button @click="childToParent">클릭!</button>
    <!-- 클릭하면 childToParent 이벤트 발생  -->
    <!-- childToParent이벤트는 child-to-parent이벤트를 발생 -->
    <input type="text" v-model="childInputData" @keyup.enter="ChildInput">
  </div>
</template>

<script>
export default {
  name: 'MyChild',
  data : function () {
    return {
      childInputData: null,
    }
  },
  props: {
    staticProps: String,
    myProps: String,
  },
  methods : {
    childToParent: function() {
      this.$emit('child-to-parent', 'child Data')
    },
    ChildInput: function(){
      this.$emit('child-input', this.childInputData)
      this.childInputData=""
    }
  }
}
</script>

<style>
  
</style>
