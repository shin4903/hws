<template>
  <div id="app" class="container text-center">
    <h1>SSAFY 상담 예약 시스템</h1>

    <div class="row"> 
    <div class="col border border-end-0 border-primary p-4 rounded-start-4">
      <h2>예약 페이지</h2>
      <h3>선생님 선택</h3>
      <button type="button" v-for="doctor in doctors" :key="doctor" class="list-item btn btn-secondary" @click="doctorselect(doctor)" :class="{'selected':isDoctor(doctor)}">{{doctor}}</button>

      <hr>
      <h3>시간 선택</h3>
      <button type="button" v-for="time in times" :key="time" @click="select(time)" class="list-item btn btn-secondary" :class="{'selected':isSelected(time)}">{{time}}</button>

    </div>
    <div class="col bg-primary-subtle border border-start-0 border-primary p-4 rounded-end-4 ">
      <h2>상담 신청 현황</h2>
      <h3>상담 선생님</h3>
      <p>성함 : {{doctorList}}</p>
      <hr>
      <h3>예약 현황</h3>
      <p>{{timeList}}</p>
      <hr>
      <img alt="Vue logo" src="./assets/ssafy-logo.png">
    </div>
  </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  methods: {
    select(time) {
      if (this.timeList.includes(time)) {
        const idx = this.timeList.indexOf(time)
        this.timeList.splice(idx,1)
      } else {
        if(this.timeList.length === 5){
          alert('5타임까지만 신청가능합니다.')
        }
        else {
          this.timeList.push(time)
        }
        
      }
    },
    isSelected(time){
      if (this.timeList.includes(time)) {
        return true
      }
      else{
        return false
      }
    },
    doctorselect(doctor) {
      if (this.doctorList.includes(doctor)) {
        const idx = this.doctorList.indexOf(doctor)
        this.doctorList.splice(idx,1)
      } else {
        if (this.doctorList.length === 1) {
          alert('의사는 1명까지만 선택가능합니다')
        } else {
          this.doctorList.push(doctor)
        }
      }
    },
    isDoctor(doctor) {
      if (this.doctorList.includes(doctor)){
        return true
      } else {
        return false
      }
    }
  },
  data() {  
    return{
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30",
        "12:00","12:30","13:00","13:30","14:00","14:30",
        "15:00","15:30","16:00","16:30","17:00","17:30",
      ],
      timeList : [],
      doctors: ["Eric", "Tony"],
      doctorList : []
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

.list-item {
  margin:10px;
  font-size: 24px;
  padding: 5px;
  cursor: pointer;
}

.selected {
  background-color: steelblue;
  color: yellow;
}
</style>
