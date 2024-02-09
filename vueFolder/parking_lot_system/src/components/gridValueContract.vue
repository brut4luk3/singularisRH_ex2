<template>
    <div class="dialog-overlay" v-if="visible">
        <div class="dialog-content">
            <h2>Detalhes do Contrato</h2>
            <p>Data de Entrada: {{ formatDate(vehicle.entry_date) }}</p>
            <p>Valor a Cobrar: {{ calculatedValue.toFixed(2) }}</p>
            <button class="btn top" @click="registerExit">Registrar Saída</button>
            <button class="btn bottom" @click="closeDialog">Fechar</button>
        </div>
    </div>
</template>
  
<script>
export default {
    props: {
        visible: Boolean,
        vehicle: Object,
    },
    data() {
        return {
            contract: null,
            calculatedValue: 0,
        };
    },
    async created() {
        await this.fetchContract();
        this.calculateValue();
    },
    methods: {
        async fetchContract() {
            try {
                const response = await fetch('http://localhost:8000/api/v1/contract/');
                if (!response.ok) throw new Error('Falha ao buscar contrato');
                const data = await response.json();
                this.contract = data.length > 0 ? data[0] : null;
                this.calculateValue();
            } catch (error) {
                console.error('Erro:', error);
            }
        },
        calculateValue() {
            if (!this.vehicle.entry_date || !this.contract) return;
            const entryTime = new Date(this.vehicle.entry_date).getTime();
            const currentTime = new Date().getTime();
            const diffMinutes = Math.round((currentTime - entryTime) / (1000 * 60));
            const valuePerMinute = this.contract.max_value / 480;
            let value = diffMinutes * valuePerMinute;
            this.calculatedValue = Math.min(value, this.contract.max_value);
        },
        formatDate(dateString) {
            const date = new Date(dateString);
            return `${date.getDate().toString().padStart(2, '0')}/${(date.getMonth() + 1).toString().padStart(2, '0')}/${date.getFullYear()}`;
        },
        closeDialog() {
            this.$emit('close');
        },
        registerExit() {
            this.$emit('exitRegistered');
        },
    },
};
</script>

<style src="@/styles/gridValueContract.css" scoped></style>