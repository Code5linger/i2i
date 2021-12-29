<template>
  <div>
    <h1 v-for="all_name in phone_book" :key="all_name">
      <p v-if="all_name.name == 'Code'" style="color:red">
        {{ all_name.name }}
      </p>
      <p v-else style="color: limegreen">
        {{ all_name.name }}
      </p>
    </h1>
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