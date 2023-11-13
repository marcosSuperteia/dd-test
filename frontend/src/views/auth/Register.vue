<template>
  <p class="text-5xl flex justify-content-center -my-5">
    Register
  </p>
  <section class="flex justify-content-center">

    <form @submit.prevent="register" class="flex flex-column w-min" :class="fadeout">

      <label for="fullname" :class="fadeout" class="col-fixed mt-5">Full Name</label>
      <InputText :autofocus=true :class="fadeout" v-model="fullname" placeholder="Full Name" required />

      <label for="username" :class="fadeout" class="col-fixed mt-2">E-mail</label>
      <InputText v-model="user" :class="[fadeout, invalidEmail]" placeholder="user@example.com" required type="email" />

      <label for="password" :class="fadeout" class="col-fixed mt-5">Password</label>
      <Password v-model="pw" toggleMask required :class="[invalidPw, fadeout]" />

      <label for="password" :class="fadeout" class="col-fixed mt-2">Confirm Password</label>
      <Password v-model="confpw" :feedback="false" toggleMask required :class="[invalidPw, fadeout]" />

      <Button :class="fadeout" label="Register" type="submit" class="mt-5" />
    </form>
  </section>
  <section class="flex justify-content-center -my-6">
    <router-link :class="fadeout" class="p-primary" to="/login">Already have an account? Login here.</router-link>
  </section>
  <section class="flex justify-content-center">
    <p :class="fadein" class="text-lg">
      Account created with success!
    </p>
  </section>
  <Toast />
</template>
<script setup>
import apiClient from '@/helpers/axios'
import { ref, onMounted } from "vue";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'

const toast = useToast();
const router = useRouter();

const user = ref("");
const fullname = ref("");
const pw = ref("");
const confpw = ref("");
const invalidPw = ref("");
const invalidEmail = ref("");
const fadeout = ref("")
const fadein = ref("hidden")
let response = ref("")

const register = async () => {
  if (!user.value.includes('.com')) {
    toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Not a valid E-mail', life: 3000 });
    invalidEmail.value = "p-invalid"
  } else {
    invalidEmail.value = ""
  }

  if (pw.value.length < 6 || pw.value.length > 20) {
    toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Password length must be greater than 6 and less than 20', life: 3000 });
    invalidPw.value = "p-invalid"
  } else {
    if (pw.value !== confpw.value) {
      toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'Passwords must be equal', life: 3000 });
      invalidPw.value = "p-invalid"
    } else {
      invalidPw.value = ""
      const data = {
        full_name: fullname.value,
        password: confpw.value,
        email: user.value,
      }

      response = await apiClient.post("users/open", data)

      if (response !== undefined && invalidPw.value == "" && invalidEmail.value == "") {
        setTimeout(() => {
          fadeout.value = "hidden";
          fadein.value = "fadeindown animation-duration-300"
        }, 300);
        toast.add({ severity: 'success', summary: 'Success', detail: 'Account created with success!', life: 3000 });
        setTimeout(() => {
          router.push("/login");
        }, 3800)
      } else if (response === undefined && invalidPw.value == "" && invalidEmail.value == "") {
        toast.add({ severity: 'error', summary: 'Failed to Register', detail: 'E-mail already in use', life: 3000 });
        invalidEmail.value = "p-invalid"
      }
    }

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