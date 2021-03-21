<template>
  <div v-if="queue === null">
    Телочки закончились
  </div>
  <div v-else>
    <Tinder ref="tinder" key-name="id" :queue.sync="queue" :offset-y="10" @submit="onSubmit">
      <template slot-scope="scope">
        <div
          class="pic"
          :style="{
            'background-image': `url(${scope.data.avatar})`
          }"
        />
        <div class="bottom-text">
          <div> {{scope.data.name}}, {{scope.data.age}} </div>
          <div> {{scope.data.description}} </div>
        </div>
      </template>
      <img class="like-pointer" :slot="false" src="@/assets/nope-txt.png">
      <img class="super-pointer" :slot="true" src="@/assets/like-txt.png">
    </Tinder>
    <div class="btns">
      <img src="@/assets/nope.png" @click="decide(false)">
      <img src="@/assets/like-txt.png" @click="decide(true)">
    </div>
  </div>
</template>

<script>
import Tinder from "vue-tinder";
import source from "@/bing";

export default {
  name: "App",
  props: {
    data: Array
  },
  components: { Tinder },
  data: () => ({
    queue: [],
    offset: 0
  }),
  created() {
    this.mock();
  },
  watch: {
    data: function () {
      //this.queue = this.data
      this.mock();
    }
  },
  methods: {
    mock(count = 5) {
      console.log(this.queue)
      this.queue = this.data
    },
    onSubmit({type, item}) {
      this.$emit('selectPair', {
        type: type,
        item: item
      })
      this.mock();
    },
    decide (choice) {
      this.$refs.tinder.decide(choice)
    }
  }
};
</script>

<style>
html,
body {
  height: 100%;
}

body {
  margin: 0;
  background-color: #20262e;
  overflow: hidden;
}

#app .vue-tinder {
  position: absolute;
  z-index: 1;
  left: 0;
  right: 0;
  top: 80px;
  margin: auto;
  width: calc(50% - 20px);
  height: calc(90% - 23px - 65px - 47px - 16px);
  min-width: 300px;
  max-width: 355px;
}

.nope-pointer,
.like-pointer {
  position: absolute;
  z-index: 1;
  top: 20px;
  width: 64px;
  height: 64px;
}

.nope-pointer {
  right: 10px;
}

.like-pointer {
  left: 10px;
}

.super-pointer {
  position: absolute;
  z-index: 1;
  bottom: 80px;
  left: 0;
  right: 0;
  margin: auto;
  width: 112px;
  height: 78px;
}

.pic {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.btns {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 30px;
  margin: auto;
  height: 65px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 300px;
  max-width: 355px;
}

.btns img {
  margin-right: 12px;
  box-shadow: 0 4px 9px rgba(0, 0, 0, 0.15);
  border-radius: 50%;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.btns img:nth-child(2n + 1) {
  width: 53px;
}

.btns img:nth-child(2n) {
  width: 65px;
}

.btns img:nth-last-child(1) {
  margin-right: 0;
}

.bottom-text {
  text-align: left;
  position: absolute;
  bottom: 20px;
  left: 10px;
  color: white;
  font-weight: 600;
  font-size: 24px;
}
</style>
