<template>
    <div class="main-menu">
        <button @click="openDialog('Veículo')">Veículo</button>
        <button @click="openDialog('Cliente')">Cliente</button>
        <button @click="openDialog('Plano')">Plano</button>
        <button @click="openDialog('Contrato')">Contrato</button>
        <DialogComponent :visible="dialogVisible" @close="closeDialog">
            <template v-slot:default>
                <VehicleForm v-if="entity === 'Veículo'" @formSubmitted="formSubmitted" />
                <ClienteForm v-if="entity === 'Cliente'" @formSubmitted="formSubmitted" />
                <PlanoForm v-if="entity === 'Plano'" @formSubmitted="formSubmitted" />
                <ContractForm v-if="entity === 'Contrato'" :contractId="existingContractId"
                    @formSubmitted="formSubmitted" />
            </template>
        </DialogComponent>
    </div>
</template>
  
<script>
import DialogComponent from './mainmenu/DialogComponent.vue';
import VehicleForm from './mainmenu/VehicleForm.vue';
import ClienteForm from './mainmenu/ClientForm.vue';
import PlanoForm from './mainmenu/PlanForm.vue';
import ContractForm from './mainmenu/ContractForm.vue';

export default {
    name: 'MainMenu',
    components: {
        DialogComponent,
        VehicleForm,
        ClienteForm,
        PlanoForm,
        ContractForm,
    },
    data() {
        return {
            entity: '',
            dialogVisible: false,
            existingContractId: '',
        };
    },
    mounted() {
        this.checkForExistingContract();
    },
    methods: {
        openDialog(entity) {
            this.entity = entity;
            this.dialogVisible = true;
        },
        closeDialog() {
            this.dialogVisible = false;
        },
        formSubmitted() {
            this.dialogVisible = false;
            if (this.entity === 'Contrato') {
                this.checkForExistingContract();
            }
        },
        async checkForExistingContract() {
            try {
                const response = await fetch('http://localhost:8000/api/v1/contract/');
                if (!response.ok) {
                    throw new Error('Falha ao verificar contratos existentes');
                }
                const contracts = await response.json();
                if (contracts.length > 0) {
                     
                    this.existingContractId = contracts[0].id;
                } else {
                    this.existingContractId = '';
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
    },
}
</script>  
  
<style src="@/styles/MainMenu.css" scoped></style>