<template>
  <div class="container">
    <div class="video-js-responsive-container vjs-hd video-container">
      <video-player :options="GetVideoOptions()" class="vjs-big-play-centered vjs-fill" width="100%" height="100%" />
    </div>

    <div class="video-information">
      <h1>{{ video.title }}</h1>
      <p>Uploaded by {{ video.user }} at {{ video.date }}</p>
      <p>Description: {{ video.description }}</p>


      <div class="input-group mb-3">
        <div class="input-group-prepend">
          <span class="input-group-text" id="inputGroup-sizing-default"><i class="bi bi-hand-thumbs-up-fill"
              style="margin-right:5px;"></i>{{
                  video.likes_count
              }}</span>
        </div>
        <button class="btn btn-outline-secondary" type="button" @click="Like()">Like</button>
      </div>

      <div class="input-group mb-3">
        <span class="input-group-text" id="inputGroup-sizing-default">{{ video.user }}</span>
        <button class="btn btn-outline-secondary" type="button" @click="Subscribe()">Subscribe</button>
      </div>

      <div class="comment-section mb-3">
        <p>Write a comment:</p>
        <div class="user-comment-container mb-3">
          <div class="input-group">
            <input v-model="comment" type="text" ref="comment" class="user-comment-textbox form-control">
            <button class="user-comment-send-button btn btn-outline-secondary"
              @click="SendComment(comment)">Send</button>
          </div>
        </div>

        <p>Other comments:</p>
        <div v-for="comm in comments" :key="comm.id" class="comment mb-3">
          <div class="comment-user">
            <img :src="comm.avatar">
            <!-- <img src="https://i.imgur.com/zx7KNAy.png"> -->
            {{ comm.user }}
          </div>
          <div class="comment-text">
            {{ comm.body }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios');
import VideoPlayer from '@/components/VideoPlayer.vue';
import 'video.js/dist/video-js.css';
export default {
  name: 'VideoView',
  components: { VideoPlayer },
  data() {
    var authkey, comment, video = this.GetVideoData(this.$route.params.id);
    return {
      video, authkey, comment, comments: []
    }
  },
  created() {
    this.authkey = this.$cookies.get('authkey')
    console.log(this.authkey)
  },
  methods: {
    GetVideoData(id) {
      const formData = new FormData();
      const headers = { 'Content-Type': 'application/json' };
      axios.get(this.backhost + '/api/videos/' + id, formData, { headers }).then((res) => {
        this.video = res.data;
        document.title = res.data.title
        // console.log(res.data)
        this.GetComments(res.data.comments)
      });
    },
    GetVideoOptions() {
      var videoOptions = {
        // width: 1280,
        // height: 720,
        aspectRatio: "16:9",
        autoplay: false,
        controls: true,
        sources: [
          {
            src: this.video.video,
            type: 'video/mp4'
          }
        ]
      }
      return videoOptions
    },
    SendComment(comment) {
      const formData = new FormData();
      formData.append('body', comment);
      formData.append('video', this.video.id);
      const headers = { 'Content-Type': 'application.json', 'Authorization': `Token ${this.authkey}` };
      axios.post(this.backhost + '/api/videos/comments/', formData, { headers }).then((res) => {
        axios.get(this.backhost + '/api/videos/comments/' + res.data.id + '/', formData, { headers }).then((res1) => this.comments.unshift(res1.data));
      });
    },
    GetComments(ids) {
      // console.log(ids)
      this.comments = []
      const formData = new FormData();
      const headers = { 'Content-Type': 'application/json' };
      for (let i = 0; i < ids.length; i++) {
        console.log(ids[i])
        axios.get(this.backhost + '/api/videos/comments/' + ids[i] + '/', formData, { headers }).then((res) => this.comments.push(res.data));
      }
      // console.log(this.comments)
    },
    Like() {
      const formData = new FormData();
      const headers = { 'Content-Type': 'application/json', 'Authorization': `Token ${this.authkey}` };
      axios.post(this.backhost + `/api/videos/${this.video.id}/likes`, formData, { headers }).then((res) => {
        console.log(res.data);
      });
      this.video.likes_count += 1;
    },
    Subscribe() {
      const formData = new FormData();
      const headers = { 'Content-Type': 'application/json', 'Authorization': `Token ${this.authkey}` };
      axios.post(this.backhost + `/api/users/${this.video.user_id}/subscribe`, formData, { headers }).then((res) => {
        console.log(res.data);
      });
    }
  }
}
</script>
<style>
.container {
  margin-top: 2em;
  margin-bottom: 2em;
  aspect-ratio: 16/9;
  display: flex;
  flex-direction: column;
  gap: 2em;
  width: 70%;
}

/* .video-description {} */

.comment-section {
  display: flex;
  flex-direction: column;
}

.comment {
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  background: rgb(243, 243, 243);
}

.comment-user {
  display: flex;
  gap: 10px;
  align-items: center;
}

.comment-user>img {
  clip-path: circle(32px at center);
  width: 32px;
  height: 32px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid black;
}
</style>