<template>
    <section>
        <router-view />
    </section>
</template>

<script setup>
import { useConfigStore } from '@/store';
import { storeToRefs } from 'pinia';
const store = useConfigStore()
const { toolbar } = storeToRefs(store);
</script>


<style>
body {
    margin: 0 !important;
    background-color: var(--surface-ground);
}
</style>