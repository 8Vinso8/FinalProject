<template>
  <div>
        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Title</span>
            </div>
            <input v-model="title" type="text" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Desc</span>
            </div>
            <input v-model="desc" type="text" class="form-control" aria-label="Default" aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <input @change="previewFiles($event, 1)" type="file" class="form-control" data-classButton="btn btn-primary" data-buttonText="Video" aria-label="Default" aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <input @change="previewFiles($event, 2)" type="file" class="form-control" data-classButton="btn btn-primary" data-buttonText="Thumbnail" aria-label="Default" aria-describedby="inputGroup-sizing-default">
        </div>
        <button class="btn btn-outline-secondary" @click="UploadRequest(title, desc, video, thumb)">Upload</button>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'UploadView',
  components: {
  },
  data(){
    var title,desc,video,thumb;
    return{
        title,desc,video,thumb
    }
  },
  methods:{
    UploadRequest(title, desc, /*video, thumb*/)
    {
        let xhr = new XMLHttpRequest();
        xhr.open("POST", "http://127.0.0.1:8000/api/videos/");

        xhr.setRequestHeader("Authorization:", "Token ad8aef3ac52c156fc388ed41283543f2521cf3fb");

        xhr.onload = () => console.log(xhr.responseText);

        let data = `{
        "title": "${title}",
        "description": "${desc}",
        "video"=@vid.mp4"
        }`;

        xhr.send(data);
    },
    previewFiles(evt, index) {
        let file=evt.target.files[0].name
        if(index==1)
            this.video=file
        if(index==2)
            this.thumb=file
  }
  }
}
</script>
<style>
    .input-group-text, #input{
        flex-direction:column
    }
    .input-group, #input{
        margin: 0 auto;
        width:25%;
        top:25%;
justify-content: center;
    }
</style>
