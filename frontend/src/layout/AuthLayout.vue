<template>
    <main>
        <router-view></router-view>
    </main>
</template>

<script setup>
import NavBar from './components/NavBar.vue';


</script>

<style scoped>
main {
    display: flex;
    flex-direction: column;
    height: 100vh;
    justify-content: center;
}
</style>