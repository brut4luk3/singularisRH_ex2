<template>
  <div class="park-index">
    <div class="header">
      <h1>Seja bem vindo ao ParkIndex!</h1>
      <h4 id="informativo">Cadastre ou edite os componentes</h4>
      <MainMenu @openDialog="openDialog" />
    </div>
    <operationsDisplay ref="operationsDisplay" />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import MainMenu from './MainMenu.vue';
import operationsDisplay from './operationsDisplay.vue';

export default {
  components: {
    MainMenu,
    operationsDisplay,
  },
  computed: {
    ...mapState(['dialogVisible', 'entity', 'plateCardInput']),
  },
  methods: {
    openDialog({ entity, plate }) {
      this.$store.dispatch('openDialog', { entity: entity, plate: plate });
    },
    closeDialog() {
      this.$store.dispatch('closeDialog');
    },
    formSubmitted() {
      this.closeDialog();
      this.$refs.operationsDisplay.loadVehicles();
    },
  },
}
</script>

<style src="@/styles/ParkIndex.css" scoped></style>