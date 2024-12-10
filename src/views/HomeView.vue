<template>
  <div class="home">
    <header>
      <nav>
        <ul>
          <li @click="navigateTo('view1')">Название 1</li>
          <li @click="navigateTo('view2')">Название 2</li>
          <li @click="navigateTo('view3')">Название 3</li>
        </ul>
      </nav>
    </header>
    <div class="content">
      <div class="title">
        <h2>Математические бои</h2>
      </div>
      <div class="auth-form">
        <h3>Авторизация</h3>
        <form @submit.prevent="login">
          <div>
            <label for="username">Логин: </label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div>
            <label for="password">Пароль: </label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit">Вход</button>
          <button type="button" @click="register">Регистрация</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  name: 'Home',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  setup() {
    const router = useRouter();
    const navigateTo = (view) => {
      router.push({ name: view });
    };

    return { navigateTo };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('https://your-api-url.com/login', {
          username: this.username,
          password: this.password
        });
        if (response.data) {
          console.log('Успешный вход:', response.data);
        } else {
          console.log('Неудачный вход');
        }
      } catch (error) {
        console.error('Ошибка при входе:', error);
      }
    },
    register() {
      console.log('Регистрация');
    }
  }
};
</script>

<style scoped>
.home {
  text-align: center;
}

nav {
  background-color: #f8f9fa;
  padding: 1rem;
}

nav ul {
  list-style: none;
  padding: 0;
}

nav li {
  display: inline;
  margin-right: 30px; /* Увеличил расстояние между кнопками */
  cursor: pointer; /* Добавил указатель при наведении */
}

.content {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.title {
  flex: 1;
  text-align: left;
}

.auth-form {
  flex: 1;
  text-align: right;
}

.auth-form form {
  display: inline-block;
}
</style>
