<template>
    <div class="operations-display">
        <div class="left-section">
            <div v-if="!showVehicleForm">
                <input class="input-field top" type="text" placeholder="Digite a placa ou cartão"
                    v-model="plateCardInput" />
                <input class="input-field bottom" type="text" placeholder="Valor a cobrar" v-model="chargeAmount"
                    disabled />
                <div class="buttons">
                    <button class="form-button top" @click="handleEntry">Entrada</button>
                    <button class="form-button bottom" @click="registerExit" :disabled="!canExit">Saída</button>
                </div>
            </div>
            <div v-if="showVehicleForm">
                <h3>Cadastrar Veículo</h3>
                <form @submit.prevent="submitNewVehicle">
                    <input class="input-field top" type="text" placeholder="Placa" v-model="newVehicle.vehicle_plate"
                        readonly />
                    <input class="input-field middle" type="text" placeholder="Modelo" v-model="newVehicle.vehicle_model" />
                    <input class="input-field middle" type="text" placeholder="Descrição"
                        v-model="newVehicle.vehicle_description" />
                    <button class="form-button bottom" type="submit">Salvar</button>
                </form>
            </div>
        </div>
        <div class="right-section">
            <h3 id="rightSectionTitle">Veículos no Pátio</h3>
            <div class="grid">
                <div class="grid-item" v-for="vehicle in vehicles" :key="vehicle.id" @click="openContractDetails(vehicle)"
                    :data-tooltip="`${vehicle.vehicle_model} ${vehicle.vehicle_description}`">
                    <p>{{ formatDate(vehicle.entry_date) }}</p>
                    <p>{{ vehicle.vehicle_plate }}</p>
                </div>
            </div>
        </div>
        <gridValueContract v-if="selectedVehicle && showDialog" :visible="showDialog" :vehicle="selectedVehicle"
            @close="showDialog = false" @exitRegistered="loadVehicles" />
    </div>
</template>
  
<script>
import gridValueContract from './gridValueContract.vue';

export default {
    components: {
        gridValueContract,
    },
    data() {
        return {
            plateCardInput: '',
            showVehicleForm: false,
            newVehicle: {
                vehicle_plate: '',
                vehicle_model: '',
                vehicle_description: '',
            },
            vehicles: [],
            showDialog: false,
            selectedVehicle: null,
        };
    },
    methods: {
        handleClose() {
            this.showDialog = false;
        },
        async handleEntry() {

            const vehicleExists = this.vehicles.some(vehicle => vehicle.vehicle_plate === this.plateCardInput);
            if (!vehicleExists) {
                this.showVehicleForm = true;
                this.newVehicle.vehicle_plate = this.plateCardInput;
            } else {
                alert('Veículo já registrado no pátio.');
            }
        },
        async submitNewVehicle() {
            try {
                const vehicleResponse = await fetch('http://localhost:8000/api/v1/vehicle/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newVehicle)
                });
                if (!vehicleResponse.ok) throw new Error('Falha ao cadastrar veículo');

                const vehicleData = await vehicleResponse.json();
                await this.registerVehicleInParkMovement(vehicleData.id);
                this.showVehicleForm = false;
                this.resetNewVehicleForm();
                alert('Veículo cadastrado e entrada registrada com sucesso!');
            } catch (error) {
                console.error('Erro:', error);
                alert('Erro ao salvar veículo.');
            }
        },
        async registerVehicleInParkMovement(vehicleId) {
            const entryDate = new Date().toISOString();
            await fetch('http://localhost:8000/api/v1/parkmovement/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    vehicle: vehicleId,
                    entry_date: entryDate,
                    exit_date: null,
                    value: null,
                }),
            });
            this.loadVehicles();
        },
        resetNewVehicleForm() {
            this.newVehicle = { vehicle_plate: '', vehicle_model: '', vehicle_description: '' };
            this.plateCardInput = '';
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            return `${date.getDate().toString().padStart(2, '0')}/${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getFullYear()}`;
        },
        async loadVehicles() {
            try {
                const response = await fetch('http://localhost:8000/api/v1/parkmovement/');
                if (!response.ok) throw new Error('Failed to fetch vehicles');
                const movements = await response.json();
                this.vehicles = await Promise.all(movements.map(async (movement) => {
                    const vehicleResponse = await fetch(`http://localhost:8000/api/v1/vehicle/${movement.vehicle}/`);
                    if (!vehicleResponse.ok) throw new Error('Failed to fetch vehicle details');
                    const vehicleData = await vehicleResponse.json();
                    return {
                        ...movement,
                        vehicle_plate: vehicleData.vehicle_plate,
                        vehicle_description: vehicleData.vehicle_description,
                        vehicle_model: vehicleData.vehicle_model,
                    };
                }));
            } catch (error) {
                console.error('Error:', error);
            }
        },
        openContractDetails(vehicle) {
            this.selectedVehicle = vehicle;
            this.showDialog = true;
        },
    },
    mounted() {
        this.loadVehicles();
    },
}
</script>
  
<style src="@/styles/operationsDisplay.css" scoped></style>