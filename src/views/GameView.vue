<template>
  <div class="container mt-5">
    <h1 class="text-center">Игровое поле 6x6</h1>
    <div class="row">
      <div 
        class="col-2 border text-center p-3" 
        v-for="i in 36" 
        :key="i"
        @click="UserMove(i)" 
      >
        <div v-if="CoinCheck(this.user.pos)>0">
          <img :src="coinImage" alt="Монета" class="coin-image" />
          <span class="coin-value">{{ CoinCheck(this.user.pos) }}</span>
        </div>
        <div v-else-if="this.user.pos === i">
          <img :src="userImage" alt="Пользователь" class="user-image" />
        </div>
      </div>
    </div>
    <div class="mt-3">
      <h3>Счет пользователя: {{ user.score }}</h3>
    </div>
    <button 
      class="btn btn-primary mt-3" 
      @click="EventStartButtonClick" 
      :disabled="gameStarted"
    >
      <i>Давайте начнем!</i>
    </button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'GameView',
  data() {
    return {
      user: {
        user_id: 0,
        score: 0,
        pos: 1, // Начальная позиция пользователя
      },
      gameStarted: false, // Флаг для отслеживания начала игры
    };
  },
  methods: {
    async CoinConstructor(value) {
      try {
        // Отправляем запрос на сервер для генерации монет
        await axios.post('/api/generate-coins', { count: value });
        console.log('Монеты сгенерированы на сервере');
      } catch (error) {
        console.error('Ошибка при генерации монет:', error);
      }
      // Для каждой сгенерированной монеты отображать ее в клетке
    },
    async CoinCheck(pos) {
      try {
        // Отправляем запрос на сервер для проверки наличия монеты
        const response = await axios.get(`/api/check-coin/${pos}`);
        return response.data.score || 0; // Возвращаем стоимость монеты, если она есть
      } catch (error) {
        console.error('Ошибка при проверке монеты:', error);
        return 0; // Если произошла ошибка, возвращаем 0
      }
    },
    async UserMove(new_pos) {
      this.user.pos = new_pos; // Обновляем позицию пользователя
      try {
        const coinScore = await this.CoinCheck(this.user.pos); // Проверяем наличие монеты на новой позиции
      } catch (error) {
        console.error('Ошибка при подборе монеты:', error);
      }
      if (this.CoinCheck(this.user.pos) > 0) {
        this.user.score += coinScore; // Увеличиваем счет пользователя
        alert(`Вы подобрали монету с ценностью: ${coinScore}`);
        await this.CoinDestructor(this.user.pos); // Удаляем монету
      } else {
        alert('Монетки в этой ячейке нет.');
      }
    },
    async CoinDestructor(pos) {
      try {
        // Отправляем запрос на сервер для удаления монеты
        await axios.delete(`/api/delete-coin/${pos}`);
        console.log(`Монета в позиции ${pos} удалена на сервере`);
      } catch (error) {
        console.error('Ошибка при удалении монеты:', error);
      }
    },

    EventStartButtonClick() {
      this.CoinConstructor(12); // Генерируем 12 монет
      this.gameStarted = true; // Устанавливаем флаг, что игра началась
    },
  },
  mounted() {
    // Инициализация или другие действия при загрузке компонента
  },
};
</script>



<style scoped>
  .coin-image {
  width: 50px; /* Ширина картинки монетки */
  height: 50px; /* Высота картинки монетки */
}


.coin-value {
  position: absolute; /* Абсолютное позиционирование для стоимости */
  top: 5px;
  left: 5px;
  font-weight: bold;
  color: #fff; /* Цвет текста */
}

.user-image {
  width: 50px; /* Ширина картинки пользователя */
  height: 50px; /* Высота картинки пользователя */
}
/* Дополнительные стили, если нужно */
</style>
