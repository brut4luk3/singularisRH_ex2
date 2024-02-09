<template>
    <div>
        <h3>Cadastrar Veículo</h3>
        <form @submit.prevent="submitForm">
            <input class="input-field top" type="text" placeholder="Placa" v-model="vehicle.vehicle_plate" />
            <input class="input-field middle" type="text" placeholder="Modelo" v-model="vehicle.vehicle_model" />
            <input class="input-field middle" type="text" placeholder="Descrição" v-model="vehicle.vehicle_description" />
            <input class="input-field bottom" type="text" placeholder="Cliente" v-model="vehicle.customer" />
            <br>
            <button class="form-button" type="submit">Cadastrar</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            vehicle: {
                vehicle_plate: '',
                vehicle_model: '',
                vehicle_description: '',
                customer: ''
            },
        };
    },
    methods: {
        async submitForm() {
            event.preventDefault();

            try {
                const response = await fetch('http://localhost:8000/api/v1/vehicle/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.vehicle)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const responseData = await response.json();
                console.log('Success:', responseData);
                alert('Veículo cadastrado com sucesso!');
                this.$emit('formSubmitted');
                this.resetForm();
            } catch (error) {
                console.error('Error:', error);
                alert('Falha ao cadastrar o veículo. Por favor, tente novamente.');
            }
        },
        resetForm() {
            this.vehicle = {
                vehicle_plate: '',
                vehicle_model: '',
                vehicle_description: '',
                customer: ''
            };
        },
    },
}
</script>
  
<style src="./globalFormStyle.css" scoped></style>