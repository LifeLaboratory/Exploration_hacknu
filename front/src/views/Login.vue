<template>
    <div class="container is-widescreen">
        <div class="login">
            <label class="label">LOGO</label>
            <div class="box">
                <div class="field">
                    <label class="label">Email</label>
                    <div class="control">
                    <input class="input" type="email" placeholder="e.g. alex@example.com">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Password</label>
                    <div class="control">
                    <input class="input" type="password" placeholder="********">
                    </div>
                </div>

                <button class="button is-primary" @click="login">Sign in</button>
            </div>
        </div>
    </div>
</template>

<script>
export default ({
    methods: {
        login () {
            console.log('12')
            this.$router.push({path: '/search'})
        }
    },
    setup() {
        
    },
})
</script>


<style scoped>
    .login {
        padding-top: 120px;
        width: 50%;
        margin: auto;
    }

    .login form {
        margin-top: 50px;
    }

    .box {
        border-radius: 15px;
    }
</style>