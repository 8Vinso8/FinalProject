<template>
  <nav>
    <div class="navbar">
      <router-link to="/" style="text-decoration: none">
        <div class="logo">
          <span style="color: black">Sea</span>
          <span style="color: green">Vid</span>
        </div>
      </router-link>
      <router-link to="/videos">Videos</router-link>
      <router-link v-if="logged_in" to="/subs">Subscriptions</router-link>
    </div>
    <div class="navbar" v-if="!logged_in">
      <router-link to="/login">Login</router-link>
      <router-link to="/register">Register</router-link>
    </div>
    <div class="navbar" v-if="logged_in">
      <router-link to="/upload">Upload</router-link>
      <span style="font-weight: bold; font-size: 150%">{{ my_user.username }}</span>
      <avatar :user_id="my_user.id" class="ava" />
    </div>
  </nav>
  <router-view />
</template>

<script>
const axios = require("axios");
import Avatar from "./components/UserAvatar.vue";
export default {
  components: { Avatar },
  data() {
    var logged_in, authkey, my_user;
    return {
      logged_in,
      authkey,
      my_user
    };
  },
  async created() {
    this.authkey = this.$cookies.get("authkey");
    this.logged_in = await this.IsLoggedIn();
  },
  methods: {
    async IsLoggedIn() {
      const headers = { "Content-Type": "application.json", Authorization: `Token ${this.authkey}` };
      try {
        var a = await axios.get(this.backhost + "/api/users/current", { headers });
        console.log(a);
        this.my_user = a.data;
        return true;
      } catch {
        return false;
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  padding: 30px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.logo {
  font-weight: bold;
  font-size: 2em;
  margin-right: 10px;
}

.navbar {
  display: flex;
  flex-direction: row;
  gap: 1em;
}

.ava {
  clip-path: circle(40px at center);
  width: 40px;
  height: 40px;
  object-fit: cover;
  border-radius: 50%;
  border: 2px solid rgba(0, 0, 0, 0.473);
}
</style>
