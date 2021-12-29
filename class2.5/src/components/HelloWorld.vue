<template>
  <div>
    <button @click="alarm_">Click Me▶</button>
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
  },
  methods: {
      alarm_(){
        alert("Test")
        this.alarm_2();
      },
      alarm_2() {
        alert("B")
      }
  }
}
</script>

<style lang="less" scoped>

</style>