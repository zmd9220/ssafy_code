<template>
  <div class="col card p-1 m-2" style="width: 18rem;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>


export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true,
    },
  },
  data: function () {
    return {
      poster: "https://image.tmdb.org/t/p/original/"+String(this.movie.poster_path),
    }
  }
}
</script>

<style>

</style>