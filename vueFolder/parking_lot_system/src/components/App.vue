<template>
  <div id="app">
    <ParkIndex/>
    <MainMenu/>
  </div>
</template>

<script>
import ParkIndex from '../components/ParkIndex.vue'
import MainMenu from '../components/MainMenu.vue'

export default {
  name: 'App',
  components: {
    ParkIndex,
    MainMenu
  }
}
</script>

<style src="@/styles/App.css" scoped></style>