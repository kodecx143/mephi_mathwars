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
            <div v-if=" coins[i] > 0">
              <img :src="require('@/assets/CoinImage.png')" alt="Монета" class="coin-image" />
            </div>
            <div v-else-if="user.pos === i">
              <img :src="require('@/assets/UserImage.png')" alt="Пользователь" class="user-image" />
            </div>
          </div>
        </div>
        <div class="mt-3 d-flex justify-content-between">
          <h3>Счет пользователя: {{ user.score }}</h3>
          <h3>Количество ходов: {{ user.turns }}</h3>
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
      <form @submit.prevent="submitAnswer">
        <div>
          <label for="taskText">Задача:</label>
          <input type="text" id="taskText" v-model="task.text" readonly />
        </div>
        <div>
          <label for="taskTurns">Стоимость задачи:</label>
          <input type="number" id="taskCost" v-model="task.turns" readonly />
        </div>
        <div>
          <label :for="'userAnswer' + task.task_id">Ваш ответ:</label>
          <input 
            :id="'userAnswer' + task.task_id" 
            v-model="user.answer" 
            type="number" 
          />
        </div>
        <div class="button-container d-flex flex-column w-100">
          <button type="button" class="btn btn-secondary mb-1" @click="NewIssue">Новая задача</button>
          <button type="button" class="btn btn-success" @click="submitAnswer" :disabled="isAnswerSubmitted">Отослать</button>
        </div>
      </form>
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
        turns: 0,
        pos: 1,
        answer: NaN
      },
      coins: Array(37).fill(0), // Массив для хранения наличия монет (индексы от 1 до 36)
      gameStarted: false, // Флаг для отслеживания начала игры
      task: {
        text: '',
        turns: 0,
        answer: 0,
        task_id: 0,
      },
      isAnswerSubmitted: false,
      message:NaN
    };
  },
  methods: {
    async CoinConstructor(value) {
      try {
        // Отправляем запрос на сервер для генерации монет
        await axios.post(`/api/generate-coin/${value}/`);
      } catch (error) {
        console.error('Ошибка при генерации монет:', error);
      }
    },
    async CoinCheck(pos) {
      try {
        const response = await axios.get(`/api/check-coin/${pos}`);
        return response.data.cost || 0; // Возвращаем стоимость монеты, если она есть
      } catch (error) {
        console.error('Ошибка при проверке монеты:', error); 
      }
      return 0;
    },
    async UserMove(new_pos) {
      if (this.PossibleTurn(new_pos)) {
        this.user.pos = new_pos;
        try {
          const coinScore = await this.CoinCheck(this.user.pos);
          if (coinScore > 0) {
            this.user.score += coinScore;
            alert("Вы подобрали монету с ценностью: ${coinScore}");
            await this.CoinDestructor(this.user.pos)
            await this.CoinConstructor(1);
          } else {
            alert('Монетки в этой ячейке нет.');
          }
        } catch (error) {
          console.error('Ошибка при подборе монеты:', error);
        }
      }
      else {
        console.log("Вы не можете попасть с данную клетку")
      }
    },
    async NewIssue() {
      try {
        const response = await axios.get('/api/new-task'); // Получаем новую задачу
        this.task = response.data; // Сохраняем задачу
        this.user.answer = null; // Сбрасываем ответ пользователя
        this.isAnswerSubmitted = false; // Разрешаем отправку ответа
        this.message = ''; // Сбрасываем сообщение
      } catch (error) {
        console.error('Ошибка при получении новой задачи:', error);
      }
    },
    async submitAnswer()
    {
      if (this.user.answer === this.task.answer) {
        this.user.turns += this.task.turns; // Увеличиваем счетчик ходов
        this.message = 'Ответ верный!';
      } else {
        this.message = 'Ответ неверный, возьмите другую задачу.';
      }
      console.log(this.message)
      this.isAnswerSubmitted = true; // Блокируем кнопку отправки
    },
    PossibleTurn(new_pos){
      x = this.user.pos;
      t = this.user.turns;
      count = (x / 6 + x % 6 - new_pos / 6 - new_pos);
      if (Math.abs(count)<=t) {
        this.user.turns -= Math.abs(count);
        return true;
      }
      return false;
    },
    async CoinDestructor(pos) {
      try {
        this.coins[pos] =0
        //await axios.post(`/api/delete-coin/${pos}`);
        //console.log(`Монета в позиции ${pos} удалена на сервере`);
      } catch (error) {
        console.error('Ошибка при удалении монеты:', error);
      }
    },
    EventStartButtonClick() {
      this.CoinConstructor(12); // Генерируем 12 монет
      this.checkCoins(); // Проверяем наличие монет после генерации
      this.gameStarted = true; // Устанавливаем флаг, что игра началась
    },
    async checkCoins() {
      const promises = [];
      for (let i = 1; i <= 36; i++) {
        promises.push(this.CoinCheck(i).then(cost => {
          this.coins[i] = cost; // Сохраняем стоимость монеты в массив
        }));
      }
      await Promise.all(promises); // Ждем завершения всех асинхронных операций
    },
  },
  mounted() {
    // Здесь можно добавить дополнительные действия при монтировании компонента
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
.button-container {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}
.btn {
  margin-top: 5px;
  margin-bottom: 5px;
  flex: 1; /* Заставляет кнопки занимать все доступное пространство */
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