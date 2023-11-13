<template class="tBone">
    <section class="flex justify-content-center -my-6">
        <router-link class="p-primary" to="/login">Login here.</router-link>
    </section>
    <p class="text-5xl flex justify-content-center -my-5">
        Confirmation Completed
    </p>
    <Toast />
</template>
<script setup>
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'


const tk = ref("");

onMounted(async () => {
    const url = new URL(window.location.href)
    const searchParams = url.searchParams
    tk.value = searchParams.get('tk');

    const data = {
        token: tk.value,
    }

    const response = await apiClient.post("users/confirm", data)

    setTimeout(() => {
        // router.push("/login");
    }, 3000)
})

</script>
  
  
<style scoped>
section {
    margin: 5rem 2.5rem;
}
</style>