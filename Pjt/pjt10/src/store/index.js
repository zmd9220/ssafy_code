import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    wishes: [],
  },
  mutations: {
    ADD_MOVIE: function (state, movieList) {
      state.movies = movieList
    },
    ADD_WISH: function (state, wish) {
      state.wishes.push(wish)
    },
    UPDATE_WISH: function (state, changedWish) {
      state.wishes = state.wishes.map(wish => {
        if (wish.id === changedWish.id) {
          return changedWish
        }
        return wish
      })
    },
  },
  actions: {
    getMovies: function (context) {
      axios.get('https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json')
        .then((response) => {
          context.commit('ADD_MOVIE', response.data)
          console.log(response.data)
      })
    },
    addMovie: function (context, content) {
      const wish = {
        id: _.uniqueId(),
        content: content,
        completed: false,
      }
      context.commit('ADD_WISH', wish)
    },
    updateWish: function (context, wish) {
      context.commit('UPDATE_WISH', { ...wish, completed: !wish.completed })
    }     
  },
})
