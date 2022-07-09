<template>
    <div class="container">
        <div class="d-flex justify-content-center align-items-center gap-3 mb-5">
            <avatar :user_id="user.id" class="avatar rounded-circle border border-dark" />
            <h1>{{ user.username }}'s videos</h1>
        </div>
        <video-list :videos="videos" />
    </div>
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
.avatar {
    width: 128px;
    height: 128px;
    object-fit: cover;
}
</style>
