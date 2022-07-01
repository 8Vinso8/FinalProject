<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  created() {
    var cooki = this.$cookies.get('authkey')
    console.log(cooki)
  }
}
</script>
