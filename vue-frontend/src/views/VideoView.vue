<template>
  <div>
    <span>{{video}}</span>
  </div>
</template>

<script>

export default {
  name: 'VideoView',
  components: {
  },
  data(){
    return{
      video:{}
    }
  },
    created(){
      let response=this.GetVideoData(this.$route.params.id)
      this.video=response
 },
  methods:{
    GetVideoData(id)
    {
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open( "GET", 'http://127.0.0.1:8000/api/videos/'+id, false ); // false for synchronous request
      xmlHttp.send( null );
      return(xmlHttp.responseText);
    },
  }
}
</script>
