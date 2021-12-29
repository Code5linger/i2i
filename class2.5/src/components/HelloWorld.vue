<template>
  <div>
    <h1 v-for="all in array" :key="all">
      {{ all }}
    </h1>
    h1
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
      ]
    }
  }
}
</script>

<style lang="less" scoped>

</style>