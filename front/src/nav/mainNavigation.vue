<template>
    <div>
        <div class="navBar">
            <div class="navItem" @click="goTo('search')">
                <b-icon
                    pack="fas"
                    icon="search"
                    size="is-small"
                />
            </div>
            <div class="navItem" @click="goTo('map')">
                <b-icon
                    pack="fas"
                    icon="map"
                    size="is-small"
                />
            </div>
            <div class="navItem" @click="goTo('profile')">
                <b-icon
                    pack="fas"
                    icon="user"
                    size="is-small"
                />
            </div>
        </div>
        <div>
            <router-view />
        </div>
    </div>
</template>

<script >
import axios from 'axios'
export default {
    methods: {
        goTo (link) {
            this.$router.push({path: `/me/${link}`})
        }
    }
}
</script>

<style>
.icon.is-small {
    width: 40px;
    height: 40px;
}


.navBar {
    height: 50px;
    background: white;
    padding-top: 8px;
}

.navBar div {
    display: inline-block;
    width: 33%;
}

.navItem:hover {
    cursor: pointer;
}
</style>
