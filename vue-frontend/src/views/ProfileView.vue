<template>
    <div class="container d-flex flex-column align-items-center gap-3">
        <avatar :user_id="me.id" class="comment-user-avatar rounded-circle border border-dark" />
        <button class="btn btn-danger" @click="Logout()">Logout</button>
    </div>
</template>

<script>
import Avatar from "@/components/UserAvatar.vue";
const axios = require("axios");
export default {
    name: "ProfileView",
    async created() {
        this.authkey = this.$cookies.get("authkey");
        this.me = await this.GetMe();
    },
    data() {
        var authkey, me;
        return {
            authkey,
            me
        };
    },
    components: { Avatar },
    methods: {
        Logout() {
            const headers = { "Content-Type": "application.json", Authorization: `Token ${this.authkey}` };
            axios.post(this.backhost + "/api/users/logout", { headers });
            this.$cookies.set("authkey", "cookie", "30d");
            this.$router.push("/");
        },
        async GetMe() {
            const headers = { "Content-Type": "application.json", Authorization: `Token ${this.authkey}` };
            return (await axios.get(this.backhost + "/api/users/current", { headers })).data;
        }
    }
};
</script>
<style scoped>
.comment-user-avatar {
    width: 256px;
    height: 256px;
    object-fit: cover;
}
</style>
