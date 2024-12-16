<template>
  <div class="container text-center mt-5">
    <h1>Добро пожаловать в игру!</h1>
    <router-link to="/game" class="btn btn-primary">Играть</router-link>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
.btn {
  margin-top: 20px;
}
</style>

