<template>
  <div>
    <div v-for="video in videos" v-bind:key="video.id"
      class="list-group-item list-group-item-action list-group-item-secondary item">
      <router-link :to="'/watch/' + video.id">
        <img :src="video.thumbnail" class="img-thumbnail float-left" />
        <span style=" font-size: 2em; position: flex; justify-content:center !important;">{{ video.title }}</span>
      </router-link>
    </div>
  </div>
</template>

<script>
const axios = require('axios');
export default {
  name: 'VideoListView',
  components: {
  },
  data() {
    return {
      videos: {}
    }
  },
  created() {
    this.authkey = this.$cookies.get('authkey')
    this.GetVideos().then((res) => this.videos = res.data.reverse())
    console.log()
  },
  methods: {
    GetVideos() {
      const formData = new FormData();
      const headers = { 'Content-Type': 'application/json' };
      return axios.get('http://127.0.0.1:8000/api/videos/', formData, { headers });
    }
  }
}
</script>

<style>
img {
  height: 120px !important;
  width: auto;
}

;

.item {
  width: 200px;
  height: 120px;
}
</style>
