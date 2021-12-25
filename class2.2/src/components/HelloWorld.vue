<template>
<div>
  <h1>Hello World!</h1>
  <h2>{{ test }}</h2>
  <h3>{{ test2 }}</h3>
  <h4>{{ test_num }}</h4>
  <h5>{{ test_array }}</h5>

  <ol>
    <li v-for="test_array in test_array" :key="test_array">
      {{ test_array }}
    </li>
    <li v-for="test_array in test_array" :key="test_array">
      {{ test_array}}
    </li>
  </ol>
</div>
</template>

<script>
export default {
  data() {
    return {
      test: "Check!",
      test2: 'Testing!',
      test_num: 17,
      test_array: [
        1,2,3,4,5,6,7
      ]
    }
  }
}
</script>

<style scoped>

</style>