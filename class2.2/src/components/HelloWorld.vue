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

  <h4 v-for="ppl in phone_book" :key="ppl">
    <p v-if="ppl.name=='Code'" style="color:blue">
      {{ ppl.name }} >>> {{ ppl.number}}
    </p>
    <p v-else style="color:purple">
      {{ ppl.name }} >>> {{ ppl.number}}
    </p>
  </h4>

  <h4 style="color:green" v-for="ppl in phone_book" :key="ppl">
    {{ ppl.name}}
  </h4>

  <h4 style="color:crimson" v-for="ppl in phone_book" :key="ppl">
    {{ ppl.number}}
  </h4>

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
      ],
      phone_book: [
        { name: 'Code', number: '011111111111'},
        { name: 'Slinger', number: '099999999999'},
        { name: 'Code', number: '011111111111'},
        { name: 'Slinger', number: '099999999999'}
      ]
    }
  }
}
</script>

<style scoped>

</style>