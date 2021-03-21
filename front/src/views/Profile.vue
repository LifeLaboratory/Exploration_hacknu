<template>
    <div>
        <div class="avatar"> 
            <img
                :src="me.avatar"
            />
        </div>
        <div class="name">
            <div>{{me.name}}</div>
            <div>{{me.description}}</div>
        </div>
        <div style="margin-top: 30px">
            <h2>Выберите ваш пол</h2>
            <b-button size="is-medium"
                style="margin-top: 10px;"
                :class="me.sex === true ? 'is-primary' : ''"
                @click="changeSex(true)"
                icon-left="male">
                Мужчина
            </b-button>
            <b-button size="is-medium"
                :class="me.sex === false ? 'is-primary' : ''"
                style="margin-top: 10px;"
                @click="changeSex(false)"
                icon-left="female">
                Девушка
            </b-button>
        </div>

        <div style="margin-top: 80px;">
            <h2>Выберите пол желаемого партнера</h2>
            <b-button size="is-medium"
                style="margin-top: 10px;"
                @click="changeSexFind(true)"
                icon-left="male">
                Мужчина
            </b-button>
            <b-button size="is-medium"
                style="margin-top: 10px;"
                @click="changeSexFind(false)"
                icon-left="female">
                Девушка
            </b-button>
        </div>
        <div class="columns buttons">
            <div class="column">
                <b-button size="is-medium"
                    icon-left="github-circle">
                </b-button>
                <div class="text">
                    что-то еще
                </div>
            </div>
            <div class="column">
                <b-button size="is-big"
                    icon-left="camera"
                    style="background: linear-gradient(45deg, #d766ec, #7957d5); color: white; height: 60px; width: 60px;"
                    >
                </b-button>
                <div class="text">
                    Добавить аватар
                </div>
            </div>
            <div class="column">
                <b-button size="is-medium"
                    icon-left="github-circle">
                </b-button>
                <div class="text">
                    Изменить информацию
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import aituBridge from '@btsd/aitu-bridge'
import {ip} from '@/cfg/setting.js'
import axios from 'axios'
export default {
    data() {
        return {
            me: {}
        }
    },
    mounted: async function () {
        let d = await axios.get(`${ip}/user/profile`,
        {
            headers: {
            'session': localStorage.getItem('id')
            }
        })
        this.me = d.data[0]

    },
    methods: {
        changeSex(sex) {
            this.me.sex = sex
        },
        changeSexFind(sex) {
            this.me.sex_find = sex
        }
    }
}
</script>
<style scoped>
    .avatar {
        margin: auto;
    }

    .avatar img {
        margin-top: 50px;
        border-radius: 100px;
        width: 120px;
        height: 120px;
    }

    .name {
        font-size: 24px;
    }

    .buttons {
        margin: auto;
        margin-top: 30px;
        max-width: 700px;
    }

    .buttons button {
        border-radius: 100px;
        height: 45px;
        width: 45px;
    }

    .text {
        font-size: 15px;
    }
</style>