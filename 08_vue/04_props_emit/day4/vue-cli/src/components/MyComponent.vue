<template>
  <div class="border">
    <h1>This is MyComponent</h1>
    <MyChild static-props="component(부모)에서 child로"
    :my-props="dynamicProps"
    @child-to-parent="parentGetEvent" 
    @child-input="getDaynamicData"
    />
    <!-- child-to-parent이벤트가 발생하면 parentGetEvent이벤트 실행 -->

  </div>
</template>

<script>
import MyChild from '@/components/MyChild'

export default {
  name: 'MyComponent',
  components: {
    MyChild,
  },
  // components의 data는 함수(function)여야한다
  data: function () {
    return {
      dynamicProps: "It is a data.."
    }
  },
  methods: {
    parentGetEvent(inputData) {
      console.log('자식 컴포넌트에서 발생한 이벤트')
      console.log(`child에서 보낸 ${inputData}를 받음`)
    },
    getDaynamicData(input) {
      console.log(`child에서 입력한 ${input}을 출력!!!!`)
    }
  }
}

</script>

<style>
  .border {
    border: solid;
  }
</style>
