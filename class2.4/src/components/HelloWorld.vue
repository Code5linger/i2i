<template>
  <div>
    <button @click="switch_">Click</button>
    {{ show }}
    <div v-show="show">
    <h1>Hello!</h1>
    
  </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      value: 'Testing!',
      string: 'CodeSlinger',
      num: 17,
      array: [
        1,2,3,4,5,6,7,8,9,0
      ],
      matrix: [
        { name:"person_A", number:"001"},
        { name:"person_B", number:"002"},
        { name:"person_C", number:"003"},
        { name:"person_D", number:"004"},
      ],
      show:0
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