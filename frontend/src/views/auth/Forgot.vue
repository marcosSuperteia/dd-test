<template>
    <p class="text-5xl flex justify-content-center -my-5">
        Reset Your Password
    </p>
    <section class="flex justify-content-center">

        <form @submit.prevent="reset" class="flex flex-column w-min">
            <label for="username" class="col-fixed" :class="fadeout">E-mail</label>
            <InputText :autofocus="true" :class="[fadeout, invalid]" v-model="user" placeholder="user@example.com" required
                type="email" />

            <Button label="Send Request" icon="pi pi-send" type="submit" class="mt-5" :class="fadeout"></Button>
        </form>
    </section>
    <section class="flex flex-column align-items-center -my-6">
        <router-link class="p-primary" :class="fadeout" to="/login">Already have an account? Login here.</router-link>
    </section>
    <section class="flex justify-content-center">
        <p :class="fadein" class="text-lg">
            Your password reset request was sent to your e-mail
        </p>
    </section>
    <Toast />
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'

const toast = useToast();
const router = useRouter();

const user = ref("");
const invalid = ref("");
const fadeout = ref("")
const fadein = ref("hidden")
const dNone = ref("")

const show = () => {
    toast.add({ severity: 'success', summary: 'A Token was Sent', detail: 'Check your E-mail Champ!', life: 3000 });
};

const reset = async () => {

    const data = {
        email: user.value
    }

    const response = await apiClient.post("/password-recovery", data)
    if (response !== undefined) {
        invalid.value = ""
        fadeout.value = "fadeoutup animation-duration-200";
        setTimeout(() => {
            fadeout.value = "hidden";
            fadein.value = "fadeindown animation-duration-300"
        }, 200);
        show()
        setTimeout(() => {
            router.push("/login");

        }, 3000)
    }else{
        toast.add({ severity: 'error', summary: 'Account Not Found', detail: "There's no account registered with this email.", life: 3000 });
        invalid.value = "p-invalid"
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