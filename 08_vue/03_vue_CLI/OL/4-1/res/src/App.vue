<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div class="card">
      <header>
        <h2>예약페이지</h2>
      </header>
      <section>
        <div class="time-table">
          <h3> 시간 선택 </h3>
            <ul class="time-table-list">
              <!-- 조건부 클래스 -->
              <!-- :class="{'className' : condition }" -->

              <li v-for="time in times" :key="time" @click="onClick(time)" class="list-item" :class="{'selected' : isSelected(time)}">{{time}}</li>
                                  <!-- v-for의 time임! -->
            </ul>
        </div>

        <div class="selected-time">
            <h3>
              선택시간 : 
            <span>{{ selectedTime }}</span>
            </h3>
        </div>
      </section>
    </div>
    
  </div>
</template>

<script>

export default {
  name: 'App',
  // 왜 data가 함수 형태고, 객체를 return 해야 하나요?
  data(){
    return{
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectedTime: [],
    }
  },
  methods : {
    onClick(time){
      // 선택된 값을 선택된 시간 목록에 추가
      if (this.selectedTime.includes(time)){
        // 이미 선택되어 있다면 목록에서 빼기
        // 내가 제거하고자 하는 대상이 몇번쨰 index에 있는지 찾아야 한다
        const idx = this.selectedTime.indexOf(time)
        // Array.splice(idx, count) -> idx번째부터 count만큼 제거한 새 배열
        this.selectedTime.splice(idx,1)
      } else {
        // 선택된적 없는 값이지만 ,이미 5개 선택되어 있으면 경고문 띄우기
        if (this.selectedTime.length === 5){
          alert('최대 5개까지 선택 가능합니다.')
          return
        }
        // 선택된적 없는 값이면 추가 하기
        this.selectedTime.push(time)

      }
    },
    isSelected(time) {
      // 선택되어 있는 상태이면 true 반환
      if (this.selectedTime.includes(time)) {
        return true
      } else {
        // 아니면 false 반환
        return false
      }
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

.time-table-list {
  display: flex;
  width: 500px;
  flex-wrap: wrap;
  list-style: none;
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
