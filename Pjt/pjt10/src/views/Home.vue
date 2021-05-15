<template>
  <div class="home d-flex justify-content-center row row-cols-1 row-cols-md-2 g-4">
    <!-- <button @click="getMovies" >버튼</button> -->
    <!-- <p>{{ movies[0] }}</p>
    <p>{{ movies }}</p> -->
    <!-- <p v-for="movie in movies" :key="movie.id">{{ movie.title }} </p> -->
    <MovieCard v-for="movie in movies" :key="movie.title" :movie="movie" />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'
// import axios from 'axios'

export default {
  name: 'Home',
  components: {
    MovieCard
  },
  // data: function () {
  //   return {
  //     movies: [],
  //   }
  // },
  methods: {
    // getMovies: function () {
    //   axios.get('https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json')
    //     .then((response) => {
    //     this.movies = response.data
    //     console.log(response.data)
    //   })
    // }
  },
  mounted: function () {
    this.$nextTick(function () {
      this.$store.dispatch('getMovies')
    })
  },
  computed: {
    ...mapState(['movies'])
  }
}
</script>
