<template>
  <div id="app" class="app">
    <div class="header">
      <h1>РОВНЫЙ ТИП</h1>
      <h2>BARBERSHOP</h2>
    </div>

    <div v-if="userData" class="user-info">
      <p>{{ userDataString }}</p>
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
      openList: false,
      userData: null,
    };
  },
  mounted() {
    if (window.Telegram && window.Telegram.WebApp) {
      window.Telegram.WebApp.ready();
      this.fetchUserData();
    } else {
      console.warn('Telegram Web App API не доступен');
    }
  },
  computed: {
    userDataString() {
      if (this.userData) {
        return `ID: ${this.userData.id}, Имя: ${this.userData.first_name}, Фамилия: ${this.userData.last_name || ''}, Username: ${this.userData.username || ''}`;
      } else {
        return 'Данные пользователя не получены.';
      }
    }
  },
  methods: {
    showBarberList() {
      this.openList = true;
    },
    hideBarberList() {
      this.openList = false;
    },
    fetchUserData() {
      if (window.Telegram && window.Telegram.WebApp) {
        try {
          this.userData = window.Telegram.WebApp.initDataUnsafe.user;
          this.sendDataToBot(); // Отправляем данные в бот
        } catch (error) {
          console.error("Error fetching user data:", error);
          this.userData = { error: "Failed to fetch user data" };
        }
      }
    },
    sendDataToBot() {
      if (window.Telegram && window.Telegram.WebApp && this.userData) {
        const data = JSON.stringify({
          type: 'userData',
          user: this.userData
        });

        try {
          window.Telegram.WebApp.sendData(data);
          console.log('Данные пользователя отправлены в бот:', data);
        } catch (error) {
          console.error('Ошибка отправки данных в бот:', error);
        }
      }
    },
  }
};
</script>

<style scoped>
  .user-info {
    margin-top: 20px;
    color: white;
    font-size: 16px;
    font-family: 'Roboto Flex', serif;
  }

  .user-info p {
    margin: 0;
    padding: 10px;
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 5px;
  }
</style>

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