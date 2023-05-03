<template>
  <div>
    <h1>App Parent</h1>
    <input type="text" v-model="parentData" @input="onParentDataInput">
    <p>AppData : {{ appData }}</p>
    <p>parentData : {{ parentData }}</p>
    <p>childData : {{ childData }}</p>
    <AppChild :app-data="appData" :parent-data="parentData" @child-input-change="onChildInputData"/>
  </div>
</template>

<script>
import AppChild from './AppChild.vue'
export default {
    name: 'AppParent',
    props: {
        appData: String
    },
    data() {
        return {
            parentData: '',
            childData: ''
        }
    },
    components: {
        AppChild
    },
    methods: {
        onChildInputData(childInputData) {
            this.childData = childInputData
            this.$emit('child-input-change', childInputData)
        },
        onParentDataInput() {
            this.$emit('parent-input-change', this.parentData)
        }
    }
}
</script>

<style>

</style>