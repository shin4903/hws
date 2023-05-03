<template>
  <div id="app">
   <h1>APP</h1>
   <!-- input에 입력되는 값을 appData에 바인딩해서 화면에 보이도록 하고싶다 -->
   <!-- 양방향 바인딩을 해주는 directive v-model을 쓴다 -->
   <!-- input의 value와 vue의 data중, 특정 속성을 양방향으로 묶어버린다 -->
   <input type="text" v-model="appData">
   <p>AppData : {{ appData }}</p>
   <p>childData : {{ childData }}</p>
   <p>parentData : {{partentData}}</p>
   <!-- 내가 가진 데이터를 prop 시켜주자 -->
   <!-- dynamic prop -> v-bind를 써서 하위 컴포넌트에 어떠한 값을 넘겨준다 -->
   <!-- 이때 이름은 kebob casw로 짓는다 -->
   <AppParent :app-data="appData" @child-input-change="onChildInputData" @parent-input-change="justabc"/>

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
      appData: '',
      childData: '',
      partentData : ''
    }
  },
  methods: {
    onChildInputData(childInputData) {
      this.childData = childInputData
    },
    justabc(parentData) {
      this.partentData = parentData
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
