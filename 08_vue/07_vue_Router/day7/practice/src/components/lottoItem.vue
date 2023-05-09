  <template>
  <div>
    <p v-for="(lottoNums,idx) in lottoNum" :key="idx">{{lottoNums}}</p>
  </div>
</template>

<script>
export default {
    name: 'lottoItem',
    props : {
      lottoNum : Array
    }
}
</script>

<style>

</style>