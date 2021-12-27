<template>
  <div>
  <!--Nest all the contents in a single div-->
  <button @click="switch_">Click</button>

  <div v-show="show">
    <h1>Hello!</h1>
  </div>

  
</div>
</template>

<script>
export default {
  data() {
    return {
      test: 'test',
      num: '1,2,3,4',
      array: [
        1,2,3,4,5,6,7,8,9
      ],
      phone_book: [
        { name: 'Code', number: '001'},
        { name: 'Slinger', number: '002'},
        { name: 'Ethereal', number: '003'},
        { name: 'Bad', number: '004'},
        { name: 'Attitude', number: '005'}
      ],
      show: 0
    }
  },
  methods: {
      switch_() {
        this.show = !this.show
      }
    }
}
</script>

<style scoped>

</style>