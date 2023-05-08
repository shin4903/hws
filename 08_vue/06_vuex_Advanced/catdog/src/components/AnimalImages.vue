<template>
  <div>
    <!-- select의 값이 바뀔 때 마다 status.status를 바꾼다 -->
    <select @change="onchange" name="status"  id="setStatus">
        <!-- 사용자에게 보여질 텍스트와 실제 사용될 value 구분 잘 해주기 -->
        <option value="all">전체</option>
        <option value="cat">고양이</option>
        <option value="dog">강아지</option>
    </select>
    <ul class="card-list">
        <!-- 모든 state.images 가져와서 반복 -->
        <!-- computed  -->
        <AnimalCard
            v-for="image in images"
            :key="image.id"
            :image="image"
        />
    </ul>
  </div>
</template>

<script>
import AnimalCard from './AnimalCard.vue'

export default {
    name : 'AnimalImages',
    components : {
        AnimalCard
    },
    computed: {
        // 종속대상의 값이 변경될 떄 새롭게 값을 계산하고, 그 결과인 함수의 반환값을 사용할 수 있게 한다.
        images() {
            return this.$store.getters.getStatusByImages
        }
    },
    methods : {
        onchange(event) {
            this.$store.dispatch('changeStatus', event.target.value)
            // this.$store.commit('CHANGE_STAUTS', event.target.value)
        }
    }
}
</script>

<style>
    .card-list {
        display:flex;
        flex-wrap:wrap;
        justify-content: space-between;

    }
</style>