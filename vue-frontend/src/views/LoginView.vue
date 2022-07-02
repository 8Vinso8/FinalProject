<template>
    <div class="container">
        <div class="input-group mb-3" style="text-align: center;">
            <!-- <span>{{ authkey }}</span> -->
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Username</span>
            </div>
            <input v-model="login" type="text" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Password</span>
            </div>
            <input v-model="password" type="password" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>
        <button class="btn btn-outline-secondary" @click="Login(login, password)">Login</button>
    </div>
</template>

<script>
const axios = require('axios');
export default {
    name: 'LoginView',
    data() {
        var login, password, authkey = '';
        return {
            login, password, authkey
        }
    },
    methods: {
        Login(usr, pw) {
            const formData = new FormData();
            formData.append('username', usr);
            formData.append('password', pw);
            const headers = { 'Content-Type': 'application/json' };
            axios.post(this.backhost + '/api/users/login/', formData, { headers }).then((res) => {
                this.authkey = res.data.key;
                console.log(res);
                if (res.statusText == "OK") {
                    this.$cookies.set('authkey', this.authkey, '30d');
                    console.log(`cookie ${this.authkey} set`);
                    alert("Logged in successfully!");
                }
            });
        }
    }
}
</script>
<style>
.container {
    width: 35%;
    justify-content: center;
}

.input-group-text {
    flex-direction: column;
}
</style>