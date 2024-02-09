<template>
    <div>
        <h3>Cadastrar Plano</h3>
        <form @submit.prevent="submitForm">
            <input class="input-field top" type="text" placeholder="Descrição" v-model="plan.plan_description" />
            <input class="input-field bottom" type="number" placeholder="Valor" v-model="plan.plan_value" />
            <br>
            <button class="form-button" type="submit">Cadastrar</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            plan: {
                plan_description: '',
                plan_value: ''
            },
        };
    },
    methods: {
        async submitForm() {
            event.preventDefault();

            try {
                const response = await fetch('http://localhost:8000/api/v1/plan/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.plan)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const responseData = await response.json();
                console.log('Success:', responseData);
                alert('Plano cadastrado com sucesso!');
                this.$emit('formSubmitted');
                this.resetForm();
            } catch (error) {
                console.error('Error:', error);
                alert('Falha ao cadastrar o plano. Por favor, tente novamente.');
            }
        },
        resetForm() {
            this.plan = {
                plan_description: '',
                plan_value: ''
            };
        },
    },
}
</script>
  
<style src="./globalFormStyle.css" scoped></style>