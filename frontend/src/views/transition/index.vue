<template>
    <div class="container">
        <ProgressSpinner />
    </div>
</template>

<script setup>
import ProgressSpinner from 'primevue/progressspinner';
import { useRouter } from 'vue-router'

const router = useRouter();

setTimeout(() => {
    router.push("/home");
}, 3000)

</script>

<style scoped>

.container {
    display: flex;
    flex-direction: column-reverse;
    position: fixed;
    height: 50%;
    width: 100%;
}



</style>