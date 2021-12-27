<template>
  <div>
    <!--Use directive to print all numbers in an array-->

    <!--
    <div v-for="x in array" :key="x">{{ x }}</div>
    -->
    <!--
    <div v-for="x in array" :key="x">{{ x }}</div>
    -->
    <!--
    <div v-for="x in array" :key="x">{{x}}</div>
    -->
    <!--
    <h1 v-for="x in array" :key="x">{{x}}</h1>
    -->
    <!--
    <h1 v-for="numbers in array" :key="numbers">{{ numbers }}</h1>
    -->

    <!--Use directive to print all the names of the phone book-->
    <!-- 
    <h1 v-for="names in phone_book.name" :key="names">{{names}}</h1>
    -->
    <!-- 
    <h1 v-for="names in phone_book" :key="names">
      {{ names.name }}
    </h1>
    -->
    <!-- 
    <h1 v-for="names in phone_book" :key="names" >
      {{ names.name }}
    </h1>
    -->
    <!-- 
    <h1 v-for="names in phone_book" :key="names">
      {{ names.name }}
    </h1>
    -->

    <!--Use directive to print all the numbers of the phone book -->
    <!--
    <h1 v-for="numbers in phone_book" :key="numbers">
      {{numbers.number}}
    </h1>
    -->
    <!--
    <h1 v-for="numbers in phone_book" :key="numbers">
      {{ numbers.number }}
    </h1>
    -->

    <!--Use directive to print all the names & numbers of the phone book -->
    <!--
    <h1 v-for="all in phone_book" :key="all">
      {{ all.name }} {{ all.number }}
    </h1>
    -->

    <!--Using directives, change colors of certain names and numbers-->
    <!--
    <h1 v-for="custom in phone_book" :key="custom">
      <p v-if="custom.name=='Code'" style="color:red">
        {{ custom.name }}
      </p>
      <p v-else style="color:black">
        {{ custom.name }}
      </p>
    </h1>
    -->
    <!--
    <h1 v-for="custom in phone_book" :key="custom">
      <p v-if="custom.name=='Code'" style="color:red">
        {{ custom.name }}
      </p>
      <p v-else style="color:gray">
        {{ custom.name }}
      </p>
    </h1>
    -->
    <!--
    <h1 v-for="custom in phone_book" :key="custom">
      <p v-if="custom.name=='Code'" style="color: red">
        {{ custom.name}}
      </p>
      <p v-else>
        {{custom.name}}
      </p>
    </h1>
    -->
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
      ]
    }
  }
}
</script>

<style scoped>

</style>