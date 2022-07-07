<template>
    <div style="display:block;">
        <div class="video-grid">
            <div v-for="video in videos" :key="video.id" class="">
                <router-link :to="'/watch/' + video.id" class="flexbox-container">
                    <img :src="video.thumbnail" class="img-thumbnail float-left thumb" />
                    <h3 class="title">{{ video.title }}</h3>
                    <div>
                        <Avatar :user_id="video.user_id" class="img-thumbnail float-left aaa" />
                        <span style=" font-size: 2em;">{{ video.user }}</span>
                    </div>
                    <div>
                        <i class="bi bi-hand-thumbs-up-fill fa-3x" style="font-size: 150%;"></i>
                        <span style=" font-size: 2em; position: flex; justify-content:center !important;">{{
                                video.likes_count
                        }}</span>
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
div {
    word-wrap: break-word;
    display: block;
}

.video-grid {
    display: flex;
    flex-direction: row;
    justify-content: center;
    flex-wrap: wrap;
}

.flexbox-container {
    max-width: 320px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 5px;
}

.title {
    font-size: 1.5em;
    overflow-wrap: break-word;
    word-wrap: break-word;
    hyphens: auto;
}

.thumb {
    width: 320px !important;
    height: auto;
    object-fit: cover;
}

.aaa {
    height: 120px !important;
    width: auto;
}

.avatar {}

;

.item {
    width: 200px;
    height: 120px;
}
</style>