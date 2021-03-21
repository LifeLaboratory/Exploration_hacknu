<template>
    <div>
        <div class="navBar">
            <div class="navItem" :class="active === 'search' ? 'active': ''" @click="goTo('search')">
                <b-icon
                    pack="fas"
                    icon="search"
                    size="is-big"
                />
            </div>
            <div class="navItem" :class="active === 'map' ? 'active': ''" @click="goTo('map')">
                <b-icon
                    pack="fas"
                    icon="map"
                    size="is-big"
                />
            </div>
            <div class="navItem" :class="active === 'profile' ? 'active': ''" @click="goTo('profile')">
                <b-icon
                    pack="fas"
                    icon="user"
                    size="is-big"
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
    data() {
        return{
            active: 'profile'
        }
    },
    methods: {
        goTo (link) {
            this.$router.push({path: `/me/${link}`})
            this.active = link
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

.active {
    color: #a21f64;
    border-bottom: 2px solid #a21f64;
    height: 100%;
}
</style>
