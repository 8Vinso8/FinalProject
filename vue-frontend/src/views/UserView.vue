<template>
    <Avatar :user_id="user.id" class="ava" />
    <span>{{ user.username }}'s videos</span>
    <video-list :videos="videos" />
</template>

<script>
const axios = require("axios");
import VideoList from "@/components/VideoList.vue";
import Avatar from "@/components/UserAvatar.vue";
export default {
    name: "UserView",
    components: { VideoList, Avatar },
    data() {
        var user, videos;
        return {
            user,
            videos
        };
    },
    async created() {
        var cooki = this.$cookies.get("authkey");
        console.log(cooki);
        this.user = await this.GetUser(this.$route.params.id);
        this.videos = await this.GetVideos(this.user.id);
    },
    methods: {
        async GetUser(id) {
            const headers = { "Content-Type": "application/json" };
            return (await axios.get(this.backhost + "/api/users/" + id, { headers })).data;
        },
        async GetVideos(id) {
            const headers = { "Content-Type": "application/json" };
            return (await axios.get(this.backhost + "/api/videos/?user=" + id, { headers })).data;
        }
    }
};
</script>
<style scoped>
.ava {
    clip-path: circle(128px at center);
    width: 128px;
    height: 128px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid rgba(0, 0, 0, 0.473);
}
</style>
