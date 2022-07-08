<template>
    <div class="container-sm d-flex flex-column gap-3">
        <div class="video-js-responsive-container vjs-hd video-container">
            <video-player
                :options="GetVideoOptions()"
                class="vjs-big-play-centered vjs-fill"
                width="100%"
                height="100%"
            />
        </div>

        <div>
            <h1>{{ video.title }}</h1>
            <p>Uploaded by {{ video.user }} at {{ video.date }}</p>
            <p>Description: {{ video.description }}</p>

            <div class="d-flex gap-3">
                <div class="input-group" style="width: auto">
                    <span class="input-group-text" id="inputGroup-sizing-default"
                        ><i class="bi bi-hand-thumbs-up-fill" style="margin-right: 5px"></i
                        >{{ video.likes_count }}</span
                    >
                    <button class="btn btn-outline-secondary" type="button" @click="Like()">Like</button>
                </div>

                <div class="input-group" style="width: auto">
                    <span class="input-group-text" id="inputGroup-sizing-default">{{ video.user }}</span>
                    <button class="btn btn-outline-secondary" type="button" @click="Subscribe()">Subscribe</button>
                </div>
            </div>
        </div>

        <div>
            <p>Write a comment:</p>
            <div class="user-comment-container my-3">
                <div class="input-group">
                    <input v-model="comment" type="text" ref="comment" class="user-comment-textbox form-control" />
                    <button class="user-comment-send-button btn btn-outline-secondary" @click="SendComment(comment)">
                        Send
                    </button>
                </div>
            </div>

            <p>Other comments:</p>
            <div class="my-3">
                <comment-list :comments="comments" />
            </div>
        </div>
    </div>
</template>

<script>
const axios = require("axios");
import VideoPlayer from "@/components/VideoPlayer.vue";
import CommentList from "@/components/CommentList.vue";
import "video.js/dist/video-js.css";

export default {
    name: "VideoView",
    components: { VideoPlayer, CommentList },
    data() {
        var authkey, comment, video;
        return {
            video,
            authkey,
            comment,
            comments: []
        };
    },
    async created() {
        this.authkey = this.$cookies.get("authkey");
        this.video = await this.GetVideoData(this.$route.params.id);
        this.comments = await this.GetComments(this.video.comments);
        document.title = this.video.title;
    },
    methods: {
        GetVideoOptions() {
            var videoOptions = {
                aspectRatio: "16:9",
                autoplay: false,
                controls: true,
                sources: [
                    {
                        src: this.video.video,
                        type: "video/mp4"
                    }
                ]
            };
            return videoOptions;
        },

        async GetVideoData(id) {
            const formData = new FormData();
            const headers = { "Content-Type": "application/json" };
            return (await axios.get(this.backhost + "/api/videos/" + id, formData, { headers })).data;
        },

        async GetComments(ids) {
            var comments = [];
            const opts = { headers: { "Content-Type": "application/json" } };
            for (let i = 0; i < ids.length; i++) {
                comments.push((await axios.get(this.backhost + "/api/videos/comments/" + ids[i] + "/", opts)).data);
            }
            return comments;
        },

        SendComment(comment) {
            this.comment = null;
            const formData = new FormData();
            formData.append("body", comment);
            formData.append("video", this.video.id);
            const headers = { "Content-Type": "application.json", Authorization: `Token ${this.authkey}` };
            axios.post(this.backhost + "/api/videos/comments/", formData, { headers }).then((res) => {
                axios
                    .get(this.backhost + "/api/videos/comments/" + res.data.id + "/", formData, { headers })
                    .then((res1) => this.comments.unshift(res1.data));
            });
        },

        Like() {
            const formData = new FormData();
            const opts = { headers: { "Content-Type": "application/json", Authorization: `Token ${this.authkey}` } };
            axios.post(this.backhost + `/api/videos/${this.video.id}/likes`, formData, opts).then(() => {
                axios.get(this.backhost + `/api/videos/${this.video.id}/likes`, opts).then((res) => {
                    this.video.likes_count += res.data.is_liked ? 1 : -1;
                });
            });
        },

        Subscribe() {
            const formData = new FormData();
            const opts = { headers: { "Content-Type": "application/json", Authorization: `Token ${this.authkey}` } };
            axios.post(this.backhost + `/api/users/${this.video.user_id}/subscribe`, formData, opts).then(() => {
                axios.get(this.backhost + `/api/users/${this.video.user_id}/subscribe`, opts).then((res) => {
                    alert(
                        res.data.is_subscribed
                            ? `Subscribed to ${(this, this.video.user)}`
                            : `Unsubscribed from ${(this, this.video.user)}`
                    );
                });
            });
        }
    }
};
</script>
