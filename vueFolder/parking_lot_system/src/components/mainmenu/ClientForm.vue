<template>
    <div>
        <h3>Cadastrar Cliente</h3>
        <form @submit.prevent="submitForm">
            <input class="input-field top" type="text" placeholder="Nome" v-model="customer.cus_name" />
            <input class="input-field bottom" type="text" placeholder="Cartão" v-model="customer.cus_card_id" />
            <br>
            <button class="form-button" type="submit">Cadastrar</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            customer: {
                cus_name: '',
                cus_card_id: ''
            },
        };
    },
    methods: {
        async submitForm() {
            // Previne o fechamento automático do diálogo
            event.preventDefault();

            try {
                const response = await fetch('http://localhost:8000/api/v1/customer/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.customer)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                // Se a operação foi bem-sucedida
                const responseData = await response.json();
                console.log('Success:', responseData);
                alert('Cliente cadastrado com sucesso!');
                this.$emit('formSubmitted'); // Emita o evento para fechar o diálogo
                this.resetForm(); // Reseta o formulário para o estado inicial
            } catch (error) {
                console.error('Error:', error);
                alert('Falha ao cadastrar o cliente. Por favor, tente novamente.');
            }
        },
        resetForm() {
            this.customer = {
                cus_name: '',
                cus_card_id: ''
            };
        },
    },
}
</script>
  
<style src="./globalFormStyle.css" scoped></style>