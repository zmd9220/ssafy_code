<template>
  <div class="random">
    <h1>오늘의 영화</h1>
    <button @click="onClick">랜덤 뽑기</button>
    <hr>
    <h2>
      <p v-text="titleText"></p>
    </h2>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'

export default {
  name: 'Random',
  data: function () {
    return {
      titleText: '',
    }
  },
  computed: {
    ...mapState(['movies'])
    // movieTitle: function () {
    //   return _.sample(movie.title)
    // }
  },
  methods: {
    onClick: function () {
      // console.log(_.sample(this.$store.state.movies).title)
      this.titleText = _.sample(this.$store.state.movies).title
    }
  }
}
</script>