<template>
    <div v-for="comment in comments" :key="comment.id" class="comment mb-3">
        <router-link :to="'/user/' + comment.user_id" style="text-decoration:none;">
            <div class="comment-user">
                <avatar :user_id="comment.user_id" class="float-left" />
                <span style="font-weight:bold">{{ comment.username }}</span>
            </div>
        </router-link>
        <div class="comment-text">
            {{ comment.body }}
        </div>
    </div>
</template>

<script>

import Avatar from './UserAvatar.vue'
export default {
    name: "CommentList",
    props: {
        comments: Array
    },
    components: { Avatar }
};
</script>

<style scoped>
.container {
    margin-top: 2em;
    margin-bottom: 2em;
    aspect-ratio: 16/9;
    display: flex;
    flex-direction: column;
    gap: 2em;
    width: 70%;
}

/* .video-description {} */

.comment-section {
    display: flex;
    flex-direction: column;
}

.comment {
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    background: rgb(243, 243, 243);
}

.comment-user {
    display: flex;
    gap: 10px;
    align-items: center;
}

.comment-user>.avatar {
    clip-path: circle(32px at center);
    width: 32px;
    height: 32px;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid black;
}
</style>