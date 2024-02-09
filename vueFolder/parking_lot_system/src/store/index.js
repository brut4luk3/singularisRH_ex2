import { createStore } from 'vuex';

export default createStore({
  state: {
    showVehicleForm: false,
    initialPlate: '',
  },
  mutations: {
    setShowVehicleForm(state, payload) {
      state.showVehicleForm = payload.show;
      state.initialPlate = payload.initialPlate || '';
    },
    openDialog(state, { entity, plate }) {
      state.dialogVisible = true;
      state.entity = entity;
      state.initialPlate = plate;
    },
    closeDialog(state) {
      state.dialogVisible = false;
      state.entity = '';
      state.initialPlate = '';
    },
  },
  actions: {
    openVehicleForm({ commit }, initialPlate) {
      commit('setShowVehicleForm', { show: true, initialPlate });
    },
    closeVehicleForm({ commit }) {
      commit('setShowVehicleForm', { show: false, initialPlate: '' });
    },
  },
});