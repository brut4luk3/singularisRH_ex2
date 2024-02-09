<template>
  <div class="park-index">
    <div class="header">
      <h1>Seja bem vindo ao ParkIndex!</h1>
      <h4 id="informativo">Cadastre e edite os componentes</h4>
      <MainMenu />
    </div>
    <div>
      <operationsDisplay />
    </div>
  </div>
</template>

<script>
import MainMenu from './MainMenu.vue'
import operationsDisplay from './operationsDisplay.vue';

export default {
  name: 'ParkIndex',
  components: {
    MainMenu,
    operationsDisplay
  }
}
</script>

<style src="@/styles/ParkIndex.css" scoped></style>