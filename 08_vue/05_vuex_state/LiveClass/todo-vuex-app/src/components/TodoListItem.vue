<template>
  <div>
    <p>{{ todoItem.title }}</p>
  </div>
</template>

<script>
export default {
    name : 'TodoListItem',
    props: {
        todoItem: Object,
    }
}
</script>

<style>

</style>