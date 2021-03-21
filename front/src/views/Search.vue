<template>
    <div class="GameCards">
        <GameCardsStack :data="userList" v-if="userList.length > 3" @selectPair="getNewPair" />
        <div v-else>
            Пользователей больше нет
        </div>
    </div>
</template>
<script>
import GameCardsStack from "../components/Card/GameCardsStack";
import aituBridge from '@btsd/aitu-bridge'
import axios from 'axios'
import {ip} from '@/cfg/setting.js'
export default {
    name: "App",
    components: {
        GameCardsStack
    },

    data() {
        return {
            can: false,
            visibleCards: [
            {
                id: 1,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            },
            {
                id: 2,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            },
            {
                id: 3,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            },
            {
                id: 4,
                photo: '',
                name: 'Roman',
                age: 20,
                interess: 'swinger'
            }
            ],
            userList: [],
            data: {}
        }
    },
    async mounted () {
        let d = await axios.get(`${ip}/user/get_next_user`,
        {
          headers: {
            'session': localStorage.getItem('id')
          }
        })
        this.userList = d.data


    },
    methods: {
        async getNewPair(data) {
            let d = await axios.post(`${ip}/user/swipe`,
            {
                id_second: data.item.id,
                status: data.type
            },
            {
            headers: {
                'session': localStorage.getItem('id')
            }
            })
            
            this.userList.push(d.data)
            if (d.data.status === 'meeting') {
                aituBridge.vibrate([500, 200, 100]);
                this.$buefy.dialog.confirm({
                    title: 'Новая пара !',
                    message: 'У вас появилось 1 совпадение, посетите страницу пар для этого',
                    confirmText: 'Просмотреть',
                    type: 'is-danger',
                    hasIcon: false,
                    onConfirm: () => this.$router.push({path: '/me/map'})
                })
            }
        },
        handleCardAccepted() {
            console.log("handleCardAccepted");
        },
        handleCardRejected() {
            console.log("handleCardRejected");
        },
        handleCardSkipped() {
            console.log("handleCardSkipped");
        },
        removeCardFromDeck() {
            this.visibleCards.shift();
        }
    }
};
</script>


<style lang="scss">
    #app {
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        text-align: center;
    }
</style>