<template>
    <div>
        <video-list :videos="videos" />
    </div>
</template>

<script>
const axios = require("axios");
import VideoList from "@/components/VideoList.vue";

export default {
    name: "SubsView",
    components: {
        VideoList
    },
    data() {
        var authkey;
        return {
            authkey,
            videos: []
        };
    },
    async created() {
        document.title = "Subscriptions";
        this.authkey = this.$cookies.get("authkey");
        console.log(this.authkey);
        this.videos = (await this.GetVideos()).data;
    },
    methods: {
        async GetVideos() {
            const options = {
                headers: { Authorization: `Token ${this.authkey}` }
            };
            return axios.get(this.backhost + "/api/videos/subscriptions/", options);
        }
    }
};
</script>
