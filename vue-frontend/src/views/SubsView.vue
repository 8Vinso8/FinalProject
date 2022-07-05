<template>
    <div class="home" style="text-align:center; position: fixed; top:40%; width: 100%;">
        <h3 style="font-size: 10em;">SeaVid</h3>
    </div>
    <div>
        <VideoList :videos="videos" />
    </div>
</template>

<script>

const axios = require('axios');
import VideoList from '@/components/VideoList.vue'

export default {
    name: 'SubsView',
    components: {
        VideoList
    },
    data() {
        var authkey
        return {
            authkey
        }
    },
    async created() {
        this.authkey = this.$cookies.get('authkey')
        this.videos = (await this.GetVideos()).data
    },
    methods: {
        async GetVideos() {
            console.log(this.authkey)
            const formData = new FormData();
            const headers = { 'Content-Type': 'application/json', 'Authorization': `Token ${this.authkey}` };
            var videos = axios.get(this.backhost + '/api/videos/subscriptions/', formData, { headers }).data.videos;
            console.log(videos)
        }
    }
}
</script>
