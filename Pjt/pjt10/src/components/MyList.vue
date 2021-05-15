<template>
    <li @click="onWishClick" :class="{completed:wish.completed}">
      <span>{{ wish.content }}</span>
    </li>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'MyList',
  computed: {
    ...mapState(['wishes']),
  },
  methods: {
    onWishClick: function () {
      this.$store.dispatch('updateWish', this.wish)
    }
  },
  props: {
    wish: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style>
  .completed{
    text-decoration: line-through;
    color: grey;
  }
</style>