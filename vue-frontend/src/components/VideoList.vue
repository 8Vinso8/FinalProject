<template>
    <div class="video-grid d-flex flex-row justify-content-center flex-wrap">
        <div v-for="video in videos" :key="video.id">
            <router-link :to="'/watch/' + video.id" class="d-flex flex-column justify-content-center p-2">
                <img :src="video.thumbnail" class="img-thumbnail float-left thumb" />
            </router-link>

            <div class="d-flex flex-row mx-3 mb-3 justify-content-between align-items-center">
                <div class="video-props d-flex flex-row gap-2">
                    <router-link :to="'/user/' + video.user_id">
                        <Avatar :user_id="video.user_id" class="avatar rounded-circle border border-dark" />
                    </router-link>

                    <div class="video-text d-flex flex-column">
                        <router-link :to="'/watch/' + video.id">
                            <b class="text-dark">{{ video.title }}</b>
                        </router-link>

                        <router-link :to="'/user/' + video.user_id">
                            <span class="text-secondary">{{ video.user }}</span>
                        </router-link>
                    </div>
                </div>
                <div class="video-likes">
                    <i class="bi bi-hand-thumbs-up-fill fa-3x"></i>
                    <span>{{ video.likes_count }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Avatar from "./UserAvatar.vue";
export default {
    name: "VideoList",
    props: {
        videos: Array
    },
    components: { Avatar }
};
</script>

<style scoped>
.thumb {
    width: 400px;
    height: auto;
    aspect-ratio: 16/9;
    object-fit: cover;
}

.avatar {
    width: 40px;
    height: 40px;
    object-fit: cover;
}

a {
    text-decoration: none;
}
</style>
