<template>
  <div id="app" class="app">
    <div class="header">
      <h1>РОВНЫЙ ТИП</h1>
      <h2>BARBERSHOP</h2>
    </div>

    <OpenButton v-if="!openList" @click="showBarberList" />

    <BarberList v-if="openList" @close="hideBarberList" ref="barberList"/>
  </div>
</template>

<script>
import BarberList from './components/BarberList.vue';
import OpenButton from './components/OpenButton.vue';

export default {
  components: {
    BarberList,
    OpenButton
  },

  data() {
    return {
      openList: false
    };
  },
  methods: {
    showBarberList() {
      this.openList = true;
    },
    hideBarberList() {
      this.openList = false;
    },
    sendDataToBot() {

    }
  }
};
</script>

<style>
  body {
  margin: 0;
  }

  .app {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100vh;
    background-image: url('@/assets/back.jpg');
    background-size: cover;
    background-position: center;
  }

  ::-webkit-scrollbar {
  width: 0px;
  }

  .header {
      margin-top: 20px;
      text-align: center;
  }

  h1, h2, h3 {
      margin: 0;
  }

  h1 {
      font-size: 35px;
      font-family: 'Roboto Slab', serif;
      color: #D0A003;
  }

  h2 {
      font-size: 30px;
      font-family: 'Roboto Flex', serif;
      color: #fff;
  }

  h3 {
      font-size: 20px;
      font-family: 'Roboto Flex', serif;
      color: #fff;
  }
</style>