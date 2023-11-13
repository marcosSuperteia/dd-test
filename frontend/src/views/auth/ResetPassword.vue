<template class="tBone">
    <p class="text-5xl flex justify-content-center -my-5">
        Enter your New Password
    </p>
    <section class="flex justify-content-center">

        <form @submit.prevent="register" class="flex flex-column w-min">

            <label for="password" class="col-fixed mt-5">Password</label>
            <Password v-model="pw" toggleMask required :class="invalidPw" />

            <label for="password" class="col-fixed mt-2">Confirm Password</label>
            <Password v-model="confpw" :feedback="false" toggleMask required :class="invalidPw" />

            <Button label="Register" type="submit" class="mt-5" />
        </form>
    </section>
    <section class="flex justify-content-center -my-6">
        <router-link class="p-primary" to="/login">Already have an account? Login here.</router-link>
    </section>
    <Toast />
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import apiClient from '@/helpers/axios'
import axios from 'axios'
import { ref, onMounted } from "vue";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'

const toast = useToast();
const router = useRouter();

const user = ref("");
const tk = ref("");
const fullname = ref("");
const pw = ref("");
const confpw = ref("");
const invalidPw = ref("");
const invalidEmail = ref("");


const register = async () => {
    const url = new URL(window.location.href)
    const searchParams = url.searchParams
    user.value = searchParams.get('email');
    tk.value = searchParams.get('tk');

    if (pw.value.length < 6 || pw.value.length > 20) {
        toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Password length must be greater than 6 and less than 20', life: 3000 });
        invalidPw.value = "p-invalid"

    } else if (pw.value !== confpw.value) {
        toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Passwords must be equal', life: 3000 });
        invalidPw.value = "p-invalid"
    } else {
        invalidPw.value = ""
        const data = {
            new_password: confpw.value,
            token: tk.value,
        }
    
        const response = await apiClient.post("reset-password", data)
    
        setTimeout(() => {
            router.push("/login");
        }, 3000)

    }



}



onMounted(() => {

})

</script>
  
  
<style scoped>
section {
    margin: 5rem 2.5rem;
}
</style>