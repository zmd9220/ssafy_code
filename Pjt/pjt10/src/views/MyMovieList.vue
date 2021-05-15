<template>
  <div>
    <MyListForm />
    <ul>
      <MyList
        v-for="wish in wishes"
        :key="wish.id"
        :wish="wish"
      />
    </ul>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm.vue'
import MyList from '@/components/MyList.vue'
import {mapState} from 'vuex'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    MyList,
  },
  computed: {
    ...mapState(['wishes']),
  },
}
</script>

<style>

</style>