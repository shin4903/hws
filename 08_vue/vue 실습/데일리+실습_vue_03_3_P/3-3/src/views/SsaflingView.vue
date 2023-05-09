<template>
  <div class="nocolor card">
    <div class="size">
      <h2>1단계</h2>
    <img src="@/assets/chevron-circle-left.png" @click="alertMessage" class="cursor">
      <img src="@/assets/happling.png" alt="" class="size2">
      <router-link to="/"><img src="@/assets/chevron-circle-right.png" alt=""></router-link>
      <h2>싸플리프</h2>
    </div>
  </div>
</template>

<script>
export default {
  name : 'SsaflingView',
  methods : {
    alertMessage() {
      alert('이전 진화 단계로 돌아갈 수 없습니다.')
    }
  }
}
</script>

<style>
.size {
  width: 300px;
  height: 300px;
}
.size2 {
  height: 100%;
  width: 100%;
  border: black;
}
.card {
  display: flex;
  justify-content: center;
  align-content: center;
}
.cursor {
  cursor: pointer;
}
</style>