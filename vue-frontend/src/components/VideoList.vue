<template>
    <div class="global-box">
        <div class="video-grid">
            <div v-for="video in videos" :key="video.id">
                <router-link :to="'/watch/' + video.id" class="video">
                    <img :src="video.thumbnail" class="img-thumbnail float-left thumb" />
                    <div class="video-props">
                        <Avatar :user_id="video.user_id" class="ava float-left" />
                        <div class="video-text">
                            <span class="video-title">{{ video.title }}</span>
                            <span class="video-author">{{ video.user }}</span>
                            <div class="video-likes">
                                <i class="bi bi-hand-thumbs-up-fill fa-3x"></i>
                                <span>{{ video.likes_count }}</span>
                            </div>
                        </div>
                    </div>

                </router-link>
            </div>
        </div>
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
.global-box {
    margin: auto;
    width: 86%;
    padding: 10px;
    max-width: 2100px;
}

.video-grid {
    display: flex;
    flex-direction: row;
    justify-content: left;
    flex-wrap: wrap;
}

.video {
    max-width: 400px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 5px;
}

.video-props {
    display: flex;
    flex-direction: row;
    justify-content: left;
    margin-top: 5px;
}

.video-text {
    display: flex;
    flex-direction: column;
    justify-content: left;
    margin-left: 10px;
}

.video-likes {
    display: flex;
    flex-direction: row;
    justify-content: left;
}

.video-title {
    color: black;
}

.video-author {
    font-size: medium;
    color: grey;
}

.thumb {
    width: 400 !important;
    height: auto;
    object-fit: cover;
}

.ava {
    clip-path: circle(32px at center);
    width: 40px;
    height: 40px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid rgba(0, 0, 0, 0.473);
}

a:link {
    text-decoration: none;
}

a:visited {
    text-decoration: none;
}

a:hover {
    text-decoration: none;
}

a:active {
    text-decoration: none;
}
</style>