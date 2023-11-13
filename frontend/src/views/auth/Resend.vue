<template>
    <p class="text-5xl flex justify-content-center -my-5">
        Resend E-mail Confirmation
    </p>
    <section class="flex justify-content-center">
        <form @submit.prevent="resend_confirmation" class="flex flex-column w-min">
            <Button icon="pi pi-send" label="Resend Confirmation" type="submit" class="mt-5" />
        </form>
    </section>
    <section class="flex flex-column align-items-center -my-6">
        <router-link class="mb-2" style="color: var(--text-color)" to="/register">Don't have an account? Register
            here</router-link>
    </section>
    <Toast />
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import { ref, onMounted } from "vue";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import apiClient from '@/helpers/axios'
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'
const email = defineProps(['email'])

const toast = useToast();
const router = useRouter();
const configure = useAuthStore();

const user = ref("");
const invalid = ref("");
const response = ref();


const resend_confirmation = async () => {
    response.value = await apiClient.post('users/resend-confirmation', {email: email.email})

}


onMounted(() => {
})

</script>
  
<style scoped>
section {
    margin: 5rem 2.5rem;
}
</style>