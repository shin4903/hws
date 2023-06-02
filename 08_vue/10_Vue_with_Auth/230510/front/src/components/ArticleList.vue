<template>
  <div>
    <p v-for="article in articleList" :key="article.created_at">
    {{article.title}} 
    {{article.content}}
    </p>

  </div>
</template>

<script>
export default {
    name: 'ArticleList',
    props : {
        articleList : Array
    }
}
</script>

<style>

</style>