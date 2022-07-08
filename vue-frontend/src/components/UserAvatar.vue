<template>
    <img :src="avatar" />
</template>

<script>
const axios = require("axios");
export default {
    name: "UserAvatar",
    props: {
        user_id: Number
    },
    async created() {
        this.avatar = (await this.GetUserAvatar(this.$props.user_id)).data.avatar;
    },
    data() {
        var avatar;
        return {
            avatar
        };
    },
    methods: {
        async GetUserAvatar(id) {
            const formData = new FormData();
            const headers = { "Content-Type": "application/json" };
            return axios.get(this.backhost + "/api/users/" + id, formData, { headers });
        }
    }
};
</script>
