<template>
  <div>
    Lorem ipsum dolor sit
    {{ abc }}
    {{ var1}}
    {{ var2 }}
    {{ num }}

    <ul>
      <li v-for="x in num" :key="x">{{num}}</li>
    </ul>

  </div>
</template>

<script>
export default {
  data () {
    return {
      abc: '!test!',
      var1: 'xx',
      var2: 'xXx',
      num: [1,2,3]
    }
  }
}
</script>