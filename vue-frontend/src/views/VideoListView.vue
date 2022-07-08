<template>
    <div>
        <video-list :videos="videos" />
    </div>
</template>

<script>
const axios = require("axios");
import VideoList from "@/components/VideoList.vue";
export default {
    name: "VideoListView",
    components: {
        VideoList
    },
    data() {
        var authkey;
        return {
            videos: {},
            authkey
        };
    },
    created() {
        document.title = "Videos";
        this.authkey = this.$cookies.get("authkey");
        this.GetVideos().then((res) => (this.videos = res.data.reverse()));
        console.log();
    },
    methods: {
        GetVideos() {
            const formData = new FormData();
            const headers = { "Content-Type": "application/json" };
            return axios.get(this.backhost + "/api/videos/", formData, { headers });
        }
    }
};
</script>
