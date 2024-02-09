<template>
  <div class="park-index">
    <div class="header">
      <h1>Seja bem vindo ao ParkIndex!</h1>
      <h4 id="informativo">Cadastre ou edite os componentes</h4>
      <MainMenu @openDialog="openDialog" />
    </div>
    <operationsDisplay ref="operationsDisplay" />
    <DialogComponent :visible="dialogVisible" @close="closeDialog">
      <template v-slot:default>
        <VehicleForm v-if="entity === 'Veículo'" :initialPlate="plateCardInput" @formSubmitted="formSubmitted" />
      </template>
    </DialogComponent>

  </div>
</template>

<script>
import { mapState } from 'vuex';
import MainMenu from './MainMenu.vue';
import operationsDisplay from './operationsDisplay.vue';
import DialogComponent from './mainmenu/DialogComponent.vue';
import VehicleForm from './mainmenu/VehicleForm.vue';

export default {
  components: {
    MainMenu,
    operationsDisplay,
    DialogComponent,
    VehicleForm,
  },
  computed: {
    ...mapState(['dialogVisible', 'entity', 'plateCardInput']), // Adicionado plateCardInput ao mapState
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
      this.$refs.operationsDisplay.loadVehicles(); // Recarrega a lista de veículos após o cadastro de um novo veículo
    },
  },
}
</script>

<style src="@/styles/ParkIndex.css" scoped></style>