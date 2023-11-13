<template>
<div class="field mt-5 mb-3">
 <InputText type="text" v-model.trim="v$.name.$model" :placeholder="$t('message.name')" />
    <div v-for="erro in v$.name.$errors" :key="erro">
        <small class="p-error">{{erro.$message}}</small>
    </div>
</div>
<div class="field mb-5"> 
    <InputText type="text" v-model.trim="v$.description.$model" :placeholder="$t('message.description')"/>
    <div v-for="erro in v$.description.$errors" :key="erro">
        <small class="p-error">{{erro.$message}}</small>
    </div>    
</div>
<div class="field"> 
<Button :label="$t('message.save')" @click="sendRole()" autofocus :disabled="v$.$invalid"/></div>
</template>
<script setup>
import { ref, defineEmits, computed } from 'vue';
import { required, helpers   } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import InputText from 'primevue/inputtext';
const name = ref()
const description = ref()

const rules = computed(() => ({
    name: {  required: helpers.withMessage('This field cannot be empty', required) },
    description: {  required: helpers.withMessage('This field cannot be empty', required) },
    }))
const v$ = useVuelidate(rules, { name, description })
const emit = defineEmits(['sendRole'])
const sendRole = () => {
    emit('sendRole', {v$})
}


// counter only uses props.initialCounter as the initial value;
// it is disconnected from future prop updates.
</script>