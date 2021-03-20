<template>
  <div id="app">
    <router-view/>
  </div>
</template>


<script>
import aituBridge from '@btsd/aitu-bridge'
export default {
  created () {

    async function getData() {
      console.log('ebash')
      try {
        // invoke method
        alert(data)
        const data = await aituBridge.getMe();
        console.log('ok', data)
        alert(data)
        // handle data
      } catch (e) {
        // handle error
        console.log('err', e);
      }
    }
    getData()
  }
}
</script>

<style>
html {
  background-color: #eae4fb !important;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
