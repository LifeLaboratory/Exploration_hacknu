<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    {{data}}
  </div>
</template>

<script>
// @ is an alias to /src
import aituBridge from '@btsd/aitu-bridge'
export default {
  name: 'Home',
  data() {
        return {
          can: false,
          data: {}
        }
  },
  components: {},
  async created () {
    this.data = await aituBridge.getMe()
  }
  
}
</script>
