<template>
    <div class="scroll">
    <section>
        <b-steps
            style="margin-top: 15px"
            v-model="activeStep"
            :animated="isAnimated"
            :rounded="isRounded"
            :has-navigation="hasNavigation"
            :icon-prev="prevIcon"
            :icon-next="nextIcon"
            :label-position="labelPosition"
            :mobile-mode="mobileMode">
            <b-step-item step="1" label="У вас новая пара!" :clickable="isStepsClickable">
                <h1 class="title has-text-centered"></h1>
                    <div class="card-flex profile-user">
                        <img :src="data.user.avatar" style="height: 40vh" />
                        <div>
                            {{data.user.name}}
                        </div>
                        <div>
                            {{data.user.description}}
                        </div>
                        <div>
                            <b>{{data.user.phone}}</b>
                        </div>
                    </div>
            </b-step-item>

            <b-step-item step="2" label="Место встречи" :clickable="isStepsClickable" :type="{'is-success': isProfileSuccess}">
                <h1 class="title has-text-centered" style="font-size: 18px">Мы подобрали вам место для встречи!</h1>
                <div class="card-flex profile-user">
                    <img :src="data.place.image" />
                    <div>
                        {{data.place.description}}
                    </div>
                    <div> Время встречи: {{formatDate(data.datetime)}} </div>
                </div>

            </b-step-item>

            <b-step-item :step="showSocial ? '4' : '3'" label="Finish" :clickable="isStepsClickable" disabled>
                <h1 class="title has-text-centered">Желаем удачи</h1>
                <div> Надеемся у вас останутся хорошие впечатления от этой встречи </div>
                <div> После встречи вам будет доступен поиск новых пар</div>
                
            </b-step-item>

            <template
                v-if="customNavigation"
                #navigation="{previous, next}">
                <div>
                <b-button
                    outlined
                    type="is-success"
                    style="width: 100px"
                    :disabled="next.disabled"
                    v-if="!next.disabled"
                    @click.prevent="next.action">
                    Далее
                </b-button>
                </div>
                <div
                    style="margin-top: 10px"
                >
                <b-button
                    outlined
                    style="width: 100px"
                    type="is-danger"
                    v-if="!previous.disabled"
                    :disabled="previous.disabled"
                    @click.prevent="previous.action">
                    Назад
                </b-button>
                </div>
            </template>
        </b-steps>
    </section>
    </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import aituBridge from '@btsd/aitu-bridge'
import {ip} from '@/cfg/setting.js'
export default {
  name: 'Home',
  data() {
        return {
          show: true,
          activeStep: 0,

        showSocial: false,
        isAnimated: true,
        isRounded: true,
        isStepsClickable: false,

        hasNavigation: true,
        customNavigation: true,
        isProfileSuccess: false,

        prevIcon: 'chevron-left',
        nextIcon: 'chevron-right',
        labelPosition: 'bottom',
        mobileMode: 'minimalist',
          can: false,
          data: {
              palace: {
                  link: 'https://cdn4.buysellads.net/uu/1/41334/1550855391-cc_dark.png'
              }
          }
        }
  },
  methods: {
      openLink(link) {
          window.open(link)
      },
      formatDate(date) {
          let d = new Date(date)


          return `${d.getDate()}/${d.getMonth()}/${d.getFullYear()} ${d.getHours()}:${d.getMinutes()}`
      }
  },
  components: {},
    async created () {
    let d = await axios.get(`${ip}/user/get_meeting`,
        {
            headers: {
            'session': localStorage.getItem('id')
            }
        })
    console.log('e')
    this.data = d.data
    this.show = false
    this.show = true
  }
  
}
</script>

<style scoped>
    .card {
        width: 90%;
        margin-left: 5%;
        padding-top: 20px;
        padding-bottom: 10px;
        background: transparent !important;
        border-radius: 12px;
        border: 1px solid purple;
    }

    .profile-user {
        text-align: center
    }

    .user-info {
        margin-top: -30px;
        margin-left: 25px;
        text-align: left;
    }

    .card-flex {
        display: inline-block;
        width: 75%;
    }

    .user-info {
        text-align: left;
    }

    .map {
        margin-top: 15px;
        margin-bottom: 15px;
    }
</style>