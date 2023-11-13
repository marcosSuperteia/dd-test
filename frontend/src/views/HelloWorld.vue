<template>
  <div>
      <button @click='teste()'>AQUi </button>
      <Button icon="pi pi-arrow-right" @click="sidebarState = true" class="mr-2" />
      <permission></permission>
  </div>  
</template>

<script setup>
import Permission from './user/permissions/index.vue'
import { useAuthStore } from '../store/auth';
import apiClient from '../helpers/axios'
import { ref, onMounted } from "vue";
const configure = useAuthStore()

const teste = async() => {
  configure.login("teste@teste.com","string")
  const response = await apiClient.get("users"); 
  console.log(response.data)
}
</script>

<style>

</style>