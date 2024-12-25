<template>
  <div class="main-container d-flex flex-column">
    <div class="game-container flex-grow-1">
        <div class="container mt-5">
        <h1 class="text-center">Игровое поле 6x6</h1>
        <div class="row">
          <div 
            class="col-2 border text-center p-3" 
            v-for="i in 36" 
            :key="i"
            @click="UserMove(i)" 
          >
            <div v-if="CoinCheck(i)>0">
              <img :src="require('@/assets/CoinImage.png')" alt="Монета" class="coin-image" />
            </div>
            <div v-else-if="user.pos === i">
              <img :src="require('@/assets/UserImage.png')" alt="Пользователь" class="user-image" />
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
    </div>
    <div class="round-container">

    </div>
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
      coin: {},
      gameStarted: false, // Флаг для отслеживания начала игры
    };
  },
  methods: {
    async CoinConstructor(value) {
      try {
        // Отправляем запрос на сервер для генерации монет
        await axios.post('/api/generate-coin', { count: value });
        const response = await axios.get('/api/constructed-coin')
      } catch (error) {
        console.error('Ошибка при генерации монет:', error);
      }
      // Для каждой сгенерированной монеты отображать ее в клетке
    },
    async CoinCheck(pos) {
      try {
        // Отправляем запрос на сервер для проверки наличия монеты с 
        const response = await axios.get(`/api/check-coin/${pos}`);
        return response.cost || 0; // Возвращаем стоимость монеты, если она есть
      } catch (error) {
        console.error('Ошибка при проверке монеты:', error); 
      }
      return 0;
    },
    async UserMove(new_pos) {
      this.user.pos = new_pos; 
      try {
        const coinScore = await this.CoinCheck(this.user.pos);
      } catch (error) {
        console.error('Ошибка при подборе монеты:', error);
      }
      if (this.CoinCheck(this.user.pos) > 0) {
        this.user.score += coinScore;
        alert(`Вы подобрали монету с ценностью: ${coinScore}`);
//        await this.CoinDestructor(this.user.pos); 
      } else {
        alert('Монетки в этой ячейке нет.');
      }
    },
///    async CoinDestructor(pos) {
//      try {
//        await axios.delete(`/api/delete-coin/${pos}`);
//        console.log(`Монета в позиции ${pos} удалена на сервере`);
//      } catch (error) {
//        console.error('Ошибка при удалении монеты:', error);
//      }
//    },
//
    EventStartButtonClick() {
      this.CoinConstructor(12); // Генерируем 12 монет
      this.gameStarted = true; // Устанавливаем флаг, что игра началась
    },
  },
  mounted() {

  },
};
</script>

<style scoped>
.container {
  max-width: 800px; /* Ограничиваем максимальную ширину контейнера */
}
.row {
  display: flex; /* Используем flexbox для выравнивания ячеек */
  flex-wrap: wrap; /* Позволяем ячейкам переноситься на следующую строку */
}
.col-2 {
  width: 16.66% !important; /* Устанавливаем ширину колонки, чтобы 6 колонок помещались в строку */
  height: 70px !important; /* Высота ячейки */
  display: flex !important; /* Используем flexbox для центрирования содержимого */
  justify-content: center !important; /* Центрируем по горизонтали */
  align-items: center !important; /* Центрируем по вертикали */
  border: 1px solid #ccc !important; /* Добавляем границу для ячейки */
}
.main-container {
  position: relative;
  height: calc(100vh - 30px); /* Занимаем высоту экрана минус отступы */
  padding-left: 20px; /* Отступ слева */
  padding-right: 50px; /* Отступ справа */
}
.game-container {
  flex-grow: 1; /* Позволяет этому контейнеру занимать оставшееся пространство */
  margin-bottom: 10px; /* Отступ между контейнерами */
}
.round-container {
  height: 30%; /* Задаем высоту для дополнительного интерфейса */
  background-color: #f8f9fa; /* Светлый фон для контраста */
  border-top: 1px solid #ccc; /* Граница сверху для отделения */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.coin-image,
.user-image {
  width: 30px; /* Ширина картинки монетки и пользователя */
  height: 30px; /* Высота картинки монетки и пользователя */
}

.coin-value {
  position: absolute; /* Абсолютное позиционирование для стоимости */
  top: 5px;
  left: 5px;
  font-weight: bold;
  color: #fff; /* Цвет текста */
}
</style>