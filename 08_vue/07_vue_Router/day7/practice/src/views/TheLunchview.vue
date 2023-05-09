<template>
  <div>
    <h1>점심 메뉴 추천</h1>
    <button @click="onClick">pickLunch</button>
    <p>{{menu}}</p>
    <input type="number" v-model="nums">
    <button @click="goLottoOnClick">GoLotto</button>
    
  </div>
</template>

<script>
import _ from 'lodash'
export default {
    name : 'TheLunchview',
    data() {
        return {
            menu : null,
            lunchMenu: ['비냉', '소고기 뭇국', '너구리', '고잡밥'],
            nums : 0
        }
    },
    methods: {
        onClick() {
            this.menu = _.sample(this.lunchMenu)
        },
        goLottoOnClick() {
            // lotto 페이지가 렌더링 되도록 router 이동
            // lottoNum에 데이터 담아서
            // const real = Number(this.nums)
            // console.log(typeof real)
            if (this.nums > 0) {
                this.$router.push({name:'lotto', params: {lottoNum:this.nums}})
            } else {
                alert('바보')
            }

            // 게시글 생성 버튼이 눌렀을 때 실행 될 메서드
                // vuex를 쓰고 있었다면 게시글 생성 actions 호출    
            // server에 게시글 생성 해달라는 post 요청을 axios로 보낸다.
                // server가 게시글 생성 후, 생성 된 게시글의 정보 (pk등) json형태로 응답한다.
                // 요청 성공 했으니 then 메서드에서 response형태의 데이터를 받는다.
                // 그렇게 응답 받은 response.data.pk -> 방금 생성된 게시글  pk정보
                // 사용자에게 그 게시글의 '/detail/:article_pk' 경로로 이동하도록 $router.push

            // detail component에서는 무슨일이?
                // route.params.article_pk 에는 특정 게시글의 pk 값이 들어있다.
                // 그 pk값으로 server GET요청 보낸다.
                // 게시글의 상세정보를 서버로부터 받아와서 화면에 그린다.

        }
    }
}
</script>

<style>

</style>