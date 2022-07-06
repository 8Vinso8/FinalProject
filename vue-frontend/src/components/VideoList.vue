<template>
    <div v-for="video in videos" :key="video.id"
        class="list-group-item list-group-item-action list-group-item-secondary item">
        <router-link :to="'/watch/' + video.id">
            <img :src="video.thumbnail" class="img-thumbnail float-left aaa" />
            <Avatar :user_id="video.user_id" class="img-thumbnail float-left aaa" />
            <span style=" font-size: 2em; position: flex; justify-content:center !important;">{{ video.title }}</span>
            <span style=" font-size: 2em; position: flex; justify-content:center !important;">{{ video.user }}</span>
            <i class="bi bi-hand-thumbs-up-fill fa-3x" style="font-size: 150%;"></i>
            <span style=" font-size: 2em; position: flex; justify-content:center !important;">{{ video.likes_count
            }}</span>
        </router-link>
    </div>
</template>

<script>

import Avatar from './UserAvatar.vue'
export default {
    name: "VideoList",
    props: {
        videos: Array
    },
    components: { Avatar }
};
</script>

<style scoped>
h3 {
    margin: 40px 0 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}

.aaa {
    height: 120px !important;
    width: auto;
}

;

.item {
    width: 200px;
    height: 120px;
}
</style>