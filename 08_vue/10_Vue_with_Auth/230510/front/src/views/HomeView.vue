<template>
  <div class="home">
    <ArticleList :article-list="articles"/>
    <button @click="GetArticles">게시글 보기</button>
  </div>
</template>

<script>
import ArticleList from '../components/ArticleList.vue'
import axios from 'axios'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    ArticleList
  },
  data() {
    return {
      articles : null
    }
  },
  methods : {
    GetArticles() {
      axios({
        method : 'get',
        url : 'https://api.themoviedb.org/3/movie/550',
        params : {
          api_key : 'b578f3012a550948ffff4885867d7cab'
        }
      })
      .then(res => {
        console.log(res)
      })
      .catch(() => {
        this.$router.push('/404')
      })
    }
  }
}
</script>
