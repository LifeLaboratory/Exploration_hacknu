<template>
    <div class="scroll">
        <div class="avatar"> 
            <img
                :src="me.avatar"
            />
        </div>

        <div class="name">
            <div>{{me.name}}</div>
        </div>
        <div style="margin-top: 10px">
            <h2><b>Выберите ваш пол</b></h2>
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

        <div style="margin-top: 30px;">
            <h2><b>Выберите пол желаемого партнера</b></h2>
            <b-button size="is-medium"
                style="margin-top: 10px;"
                :class="me.sex_find === true ? 'is-primary' : ''"
                @click="changeSexFind(true)"
                icon-left="male">
                Мужчина
            </b-button>
            <b-button size="is-medium"
                style="margin-top: 10px;"
                :class="me.sex_find === false ? 'is-primary' : ''"
                @click="changeSexFind(false)"
                icon-left="female">
                Девушка
            </b-button>
        </div>
        <div>
            <b-field label="О себе" style="width: 80%; margin-left: 10%; margin-top: 20px">
                <b-input maxlength="100" v-model="me.description" type="textarea"></b-input>
            </b-field>
        </div>
        <div class="greenColors" v-if="show"> Настройки успешно сохранены !</div>
        <br />
        <b-button @click="saveProf()" icon-left="save" style="background: #a31f63; color: white">
            <b>Сохранить</b>
        </b-button>
    </div>
</template>

<script>
import {ip} from '@/cfg/setting.js'
import axios from 'axios'
export default {
    data() {
        return {
            me: {},
            show: false,
            desc: '123'
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
        async snedNewInfo() {
            let d = await axios.post(`${ip}/user/profile`,
            this.me,
            {
                headers: {
                'session': localStorage.getItem('id')
                }
            })
        },
        async saveProf() {
            await this.snedNewInfo()
            this.show = true
        },
        changeSex(sex) {
            this.me.sex = sex
            this.snedNewInfo()
        },
        changeSexFind(sex) {
            this.me.sex_find = sex
            this.snedNewInfo()
        }
    }
}
</script>
<style scoped>
    .avatar {
        margin: auto;
    }

    .avatar img {
        margin-top: 12px;
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

    .scroll {
        overflow-y: auto;
    }

    .greenColors {
        color: green
    }
</style>