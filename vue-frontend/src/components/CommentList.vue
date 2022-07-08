<template>
    <div v-for="comment in comments" :key="comment.id" class="comment d-flex flex-column gap-2 my-3 p-3 bg-light">
        <div class="comment-user d-flex gap-2 align-items-center">
            <avatar :user_id="comment.user_id" class="comment-user-avatar rounded-circle border border-dark" />
            <router-link :to="'/user/' + comment.user_id" class="text-decoration-none">
                <span style="font-weight: bold">{{ comment.username }}</span>
            </router-link>
        </div>
        <div class="comment-text">
            {{ comment.body }}
        </div>
    </div>
</template>

<script>
import Avatar from "./UserAvatar.vue";
export default {
    name: "CommentList",
    props: {
        comments: Array
    },
    components: { Avatar }
};
</script>

<style scoped>
.comment-user-avatar {
    width: 32px;
    height: 32px;
    object-fit: cover;
}
</style>
