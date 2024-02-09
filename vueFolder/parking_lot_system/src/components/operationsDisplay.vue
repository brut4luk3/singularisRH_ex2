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
                    :data-tooltip="`${vehicle.vehicle_model} ${vehicle.vehicle_description}`">
                    <p>{{ formatDate(vehicle.entry_date) }}</p>
                    <p>{{ vehicle.vehicle_plate }}</p>
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

        async fetchData(url) {
            try {
                const response = await fetch(url);
                if (!response.ok) throw new Error('Failed to fetch data');
                return await response.json();
            } catch (error) {
                console.error('Error fetching data:', error);
                throw error;
            }
        },

        async findVehicleOrCustomer() {
            const vehiclesData = await this.fetchData('http://localhost:8000/api/v1/vehicle/');
            let vehicle = vehiclesData.find(v => v.vehicle_plate === this.plateCardInput);

            if (!vehicle) {
                const customersData = await this.fetchData('http://localhost:8000/api/v1/customer/');
                let customer = customersData.find(c => c.cus_card_id === this.plateCardInput);

                if (customer) {
                    // Encontrar veículo associado ao cliente
                    let vehicle = vehiclesData.find(v => v.customer === customer.id);
                    if (vehicle) {
                        this.registerVehicleEntry(vehicle.id);
                        return;
                    }
                }

                alert('Veículo não encontrado, vamos cadastrá-lo.')

                // Se nenhum veículo ou cliente com cus_card_id foi encontrado, abre o formulário para cadastro
                this.$store.dispatch('openDialog', { entity: 'Veículo', plate: this.plateCardInput });
            } else {
                this.registerVehicleEntry(vehicle.id);
            }
        },

        async registerEntry() {
            this.findVehicleOrCustomer();
        },

        async registerVehicleEntry(vehicleId) {
            const entryDate = new Date().toISOString();
            try {
                const response = await fetch('http://localhost:8000/api/v1/parkmovement/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        vehicle: vehicleId,
                        entry_date: entryDate,
                        exit_date: null,
                        value: null,
                    }),
                });
                if (!response.ok) throw new Error('Falha ao registrar entrada do veículo');
                alert('Entrada registrada com sucesso!');
                this.loadVehicles();
            } catch (error) {
                console.error('Error:', error);
                alert('Falha ao registrar entrada.');
            }
        },

        formatDate(dateString) {
            const date = new Date(dateString);
            return `${date.getDate().toString().padStart(2, '0')}/${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getFullYear()}`;
        },
    },

    mounted() {
        this.loadVehicles();
    },
}
</script>
  
<style src="@/styles/operationsDisplay.css" scoped></style>