<template>
    <div class="operations-display">
        <div class="left-section">
            <input class="input-field top" type="text" placeholder="Digite a placa ou cartão" v-model="plateCardInput" />
            <input class="input-field bottom" type="text" placeholder="Valor a cobrar" v-model="chargeAmount" disabled />
            <div class="buttons">
                <button class="form-button top" @click="registerEntry">Entrada</button>
                <button class="form-button bottom" @click="registerExit" :disabled="!canExit">Saída</button>
            </div>
        </div>
        <div class="right-section">
            <h3 id="rightSectionTitle">Veículos no Pátio</h3>
            <div class="grid">
                <div class="grid-item" v-for="vehicle in vehicles" :key="vehicle.id"
                    :data-tooltip="`Placa: ${vehicle.plate}`">
                    <p>{{ vehicle.entry_date }}</p>
                    <p>{{ vehicle.plate }}</p>
                    <p>{{ vehicle.card_id }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            plateCardInput: '',
            chargeAmount: '',
            vehicles: [],
            canExit: false,
        };
    },
    methods: {
        async loadVehicles() {
            try {
                const response = await fetch('http://localhost:8000/api/v1/parkmovement/');
                if (!response.ok) throw new Error('Failed to fetch vehicles');
                this.vehicles = await response.json();
            } catch (error) {
                console.error('Error:', error);
            }
        },
        async registerEntry() {
            try {
                const response = await fetch('http://localhost:8000/api/v1/vehicle_entry/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ plate: this.plateCardInput }),
                });
                if (!response.ok) throw new Error('Failed to register entry');
                alert('Entrada registrada com sucesso!');
                this.loadVehicles(); // Recarrega os veículos no pátio
            } catch (error) {
                console.error('Error:', error);
                alert('Falha ao registrar entrada.');
            }
        },
        async registerExit() {
            // Implemente a lógica para registrar a saída similar ao método de entrada
        },
    },
    mounted() {
        this.loadVehicles();
    },
}
</script>  
  
<style src="@/styles/operationsDisplay.css" scoped></style>