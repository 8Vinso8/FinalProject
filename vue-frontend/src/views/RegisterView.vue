<template>
    <div class="container">
        <div class="input-group mb-3" style="text-align: center;">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Username</span>
            </div>
            <input v-model="username" type="text" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3" style="text-align: center;">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">E-mail</span>
            </div>
            <input v-model="email" type="text" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Password</span>
            </div>
            <input v-model="password1" type="password" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <div class="input-group mb-3">
            <div class="input-group-prepend col-2">
                <span class="input-group-text" id="inputGroup-sizing-default">Confirm</span>
            </div>
            <input v-model="password2" type="password" class="form-control" aria-label="Default"
                aria-describedby="inputGroup-sizing-default">
        </div>

        <button class="btn btn-outline-secondary"
            @click="Register(username, email, password1, password2)">Register</button>
    </div>
</template>

<script>
const axios = require('axios');
export default {
    name: 'RegisterView',
    data() {
        var username, email, password1, password2, authkey = '';
        return {
            username, email, password1, password2, authkey
        }
    },
    methods: {
        Register(username, email, password1, password2) {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('email', email);
            formData.append('password1', password1);
            formData.append('password2', password2);
            const headers = { 'Content-Type': 'application/json' };
            axios.post(this.backhost + '/api/users/register/', formData, { headers }).then((res) => {
                console.log(res);
                if (res.statusText == "OK") {
                    alert("Registered successfully! Check your e-mail");
                }
            });
        },
        // CheckIfUsernameAvailable(username) {

        // },
        // CheckIfEmailAvailable(email) {

        // }
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