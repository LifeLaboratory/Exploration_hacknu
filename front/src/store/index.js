import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import aituBridge from '@btsd/aitu-bridge'
import {ip} from '@/cfg/setting.js'
import router from '../router/index.js'

Vue.use(Vuex)


async function getProfile () {
  const data = await aituBridge.getMe()
  localStorage.setItem('id', data.id)
  const phone = await aituBridge.getPhone()
  return await axios.post(`${ip}/user/login`, {
    name: data.name,
    phone: phone.phone,
    lastname: data.lastname ? data.lastname : ''
  },
  {
    headers: {
      'session': data.id
    }
  })
}
export default new Vuex.Store({
  state: {
    listUser: []
  },
  mutations: {
    setList (d, k) {
      alert(d)
      alert(k)
      state.listUser = [1,2,3]
    }
  },
  actions: {
    async sendProfile (state) {
      let data = await getProfile()
      let u = 'status'
     // alert(JSON.stringify(data.data.status))
      //router.push({path: '/me/profile'})
    },

    async getUserList (context) {
      let d = await axios.get(`${ip}/user/get_next_user`,
      {
        headers: {
          'session': localStorage.getItem('id')
        }
      })
      alert(JSON.stringify(d.data))
      context.commit('setList', d.data)


    
    }
    
  },
  getters: {
    getUsers: state => {
      return state.listUser
    }
  },
  modules: {
  }
})
