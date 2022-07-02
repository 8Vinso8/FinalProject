import '@babel/polyfill'
import 'mutationobserver-shim'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-icons/font/bootstrap-icons.css'
import VueCookies from "vue-cookies";

const app = createApp(App);
app.config.globalProperties.backhost = window.location.protocol + '//' + window.location.host + ':8000';
app.use(VueCookies).use(router).mount('#app');