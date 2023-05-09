<template>
  <div class="nocolor card">
    <div class="size">
    <h2>시작</h2>
      
      <router-link to="/"><img src="@/assets/chevron-circle-left.png" alt=""></router-link>
      <img src="@/assets/happeed.png" alt="" class="size2">
      <router-link :to="{name:'ssafling'}"><img src="@/assets/chevron-circle-right.png" alt=""></router-link>

      <h2>해피드</h2>
    </div>
  </div>
</template>

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
</style>