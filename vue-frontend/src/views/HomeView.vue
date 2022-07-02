<template>
  <div class="home" style="text-align:center; position: fixed; top:40%; width: 100%;">
    <h3 style="font-size: 10em;">SeaVid</h3>
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'HomeView',
  created() {
    // var cooki = this.$cookies.get('authkey')
    console.log(this.$route.fullPath)
    console.log(this.backhost)
  }
}
</script>
