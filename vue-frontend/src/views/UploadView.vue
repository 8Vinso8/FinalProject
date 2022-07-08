<template>
    <div style="text-align: center;">
        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Title</span>
            </div>
            <input v-model="title" type="text" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Desc</span>
            </div>
            <input v-model="desc" type="text" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="mb-3">
            Upload your video:
        </div>

        <div class="input-group mb-3">
            <input @change="previewFiles(1)" type="file" ref="vid" class="form-control"
                data-classButton="btn btn-primary" data-buttonText="Video" aria-label="Default"
                aria-describedby="inputGroup-sizing-default" accept=".mp4">
        </div>

        <div class="mb-3">
            Upload your thumbnail:
        </div>

        <div class="input-group mb-3">
            <input @change="previewFiles(2)" type="file" ref="thumb" class="form-control"
                data-classButton="btn btn-primary" data-buttonText="Thumbnail" aria-label="Default"
                aria-describedby="inputGroup-sizing-default" accept=".png,.jpg,.jpeg">
        </div>
        <button class="btn btn-outline-secondary" @click="UploadRequest(title, desc, video, thumb)">Upload</button>
    </div>
</template>

<script>
// @ is an alias to /src
const axios = require('axios');
export default {
    name: 'UploadView',
    components: {
    },
    data() {
        var title, desc, video, thumb, authkey;
        return {
            title, desc, video, thumb, authkey
        }
    },
    created() {
        this.authkey = this.$cookies.get('authkey')
    },
    methods: {
        UploadRequest(title, desc, video, thumb) {
            const formData = new FormData();
            formData.append('video', video);
            console.log(thumb)
            if (typeof thumb !== 'undefined') {
                formData.append('thumbnail', thumb);
            }
            formData.append('title', title);
            formData.append('description', desc);
            const headers = { 'Content-Type': 'multipart/form-data', 'Authorization': `Token ${this.authkey}` };
            axios
                .post(this.backhost + '/api/videos/', formData, { headers })
                .then((res) => {
                    alert("Uploaded!");
                    return console.log(res)
                });
        },
        previewFiles(index) {
            if (index == 1) {
                this.video = this.$refs.vid.files[0]
                console.log(this.video)
            }
            if (index == 2) {
                this.thumb = this.$refs.thumb.files[0]
                console.log(this.thumb)
            }
        }
    }
}
</script>
<style>
.input-group-text,
#input {
    flex-direction: column
}

.input-group,
#input {
    margin: 0 auto;
    width: 25%;
    top: 25%;
    justify-content: center;
}
</style>
