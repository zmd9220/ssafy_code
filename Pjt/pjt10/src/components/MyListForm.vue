<template>
  <div>
    <input type="text" v-model="content" @keyup.enter="onEnter">
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function () {
    return {
      content: '',
    }
  },
  methods: {
    onEnter: function () {
      this.$store.dispatch('addMovie', this.content)
      this.content = ''
    }
  }
}
</script>

<style>

</style>