<template>
  <div>
    <button @click="switch_">Click ME</button>
    <h1 v-show="show">
        Hello!
      </h1>
    {{ show }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      test: "abc",
      num: 17,
      array: [
        1,2,3,4,"a","b","C","D"
      ],
      phone_book: [
        { name: 'Code', number: '001'},
        { name: 'AA', number: '002'},
        { name: 'BB', number: '003'},
        { name: 'CC', number: '004'},
      ],
      show: 0,
    }
  },
  methods: {
    switch_() {
      this.show = !this.show
    }
  }
}
</script>

<style lang="less" scoped>

</style>