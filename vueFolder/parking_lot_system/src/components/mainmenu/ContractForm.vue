<template>
    <div>
        <h3>{{ contractId ? 'Editar' : 'Cadastrar' }} Contrato</h3>
        <form @submit.prevent="submitForm">
            <input class="input-field top" type="text" placeholder="Descrição" v-model="contract.contract_description" />
            <input class="input-field bottom" type="number" placeholder="Valor Máximo" v-model="contract.contract_max_value" />
            <br>
            <button class="form-button" type="submit">{{ contractId ? 'Salvar' : 'Cadastrar' }}</button>
        </form>
    </div>
</template>

<script>
export default {
    props: {
        contractId: {
            type: String,
            default: ''
        }
    },
    data() {
        return {
            contract: {
                contract_description: '',
                contract_max_value: '',
            },
        };
    },
    mounted() {
        // Se estiver editando, carregue os dados existentes do contrato aqui
        if (this.contractId) {
            this.loadExistingContract();
        }
    },
    methods: {
        async loadExistingContract() {
            try {
                const response = await fetch(`http://localhost:8000/api/v1/contract/${this.contractId}/`);
                if (!response.ok) {
                    throw new Error('Falha ao carregar os detalhes do contrato existente');
                }
                const contractData = await response.json();
                this.contract = { // Assumindo que a resposta da API corresponda à estrutura de dados do contrato
                    contract_description: contractData.contract_description,
                    contract_max_value: contractData.contract_max_value,
                };
            } catch (error) {
                console.error('Error:', error);
                alert('Não foi possível carregar os detalhes do contrato.');
            }
        },
        async submitForm() {
            const method = this.contractId ? 'PUT' : 'POST';
            const url = this.contractId ? 
                `http://localhost:8000/api/v1/contract/${this.contractId}/` :
                'http://localhost:8000/api/v1/contract/';

            try {
                const response = await fetch(url, {
                    method: method,
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(this.contract)
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const responseData = await response.json();
                console.log('Success:', responseData);
                alert(`Contrato ${this.contractId ? 'atualizado' : 'cadastrado'} com sucesso!`);
                this.$emit('formSubmitted');
                if (!this.contractId) this.resetForm(); // Só reseta o formulário se for um cadastro novo
            } catch (error) {
                console.error('Error:', error);
                alert('Falha ao salvar o contrato. Por favor, tente novamente.');
            }
        },
        resetForm() {
            this.contract = {
                contract_description: '',
                contract_max_value: '',
            };
        },
    },
}
</script>

<style src="./globalFormStyle.css" scoped></style>