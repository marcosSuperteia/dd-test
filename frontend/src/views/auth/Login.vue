<template>
  <main :class="fadeout">

    <p class="text-5xl flex justify-content-center -my-5">
      Login
    </p>
    <section class="flex justify-content-center">
      <form @submit.prevent="login" class="flex flex-column w-min">

        <label for="username" class="col-fixed">E-mail</label>
        <InputText :autofocus="true" :class="invalid" v-model="user" placeholder="user@example.com" required
          type="email" />

        <label for="password" class="col-fixed mt-5">Password</label>
        <Password v-model="pw" :class="invalid" :feedback="false" toggleMask required />

        <Button icon="pi pi-send" label="Log In" type="submit" class="mt-5" />
      </form>
    </section>
    <section class="flex flex-column align-items-center -my-6">
      <router-link class="mb-2" style="color: var(--text-color)" to="/register">Don't have an account? Register
        here</router-link>
      <router-link class="my-2" style="color: var(--text-color)" to="/password-recovery">Forgot your
        password?</router-link>
    </section>
  </main>
  <Toast />
  <div :class="fadein">
    <Resend :email="user" v-if="resend" />
  </div>
</template>
<script setup>
import { useAuthStore } from '@/store/auth';
import { ref, onMounted } from "vue";
import InputText from 'primevue/inputtext';
import Toast from 'primevue/toast';
import { useToast } from 'primevue/usetoast';
import { useRouter } from 'vue-router'
import axios from 'axios'
import Resend from './Resend.vue';

const toast = useToast();
const router = useRouter();
const configure = useAuthStore();

const user = ref("");
const pw = ref("");
const invalid = ref("");
const response = ref();
const resend = ref(false)
const loginComponent = ref(true)
const fadeout = ref("")
const fadein = ref("hidden")



const show = () => {
  toast.add({ severity: 'error', summary: 'Failed to Log In', detail: 'Incorrect Email or Password', life: 3000 });
};

const login = async () => {
  if (user.value !== "" && pw.value !== "") {

    var data = {
      grant_type: "",
      username: user.value,
      password: pw.value,
      scope: "",
      client_id: "",
      client_secret: "",
    };

    var config = {
      method: "post",
      url: import.meta.env.VITE_SERVER_NAME + "login/access-token",
      headers: {
        accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      data: data,
    };

    try {
      const userData = await axios(config);
      response.value = await configure.login(user.value, pw.value);
      toast.add({ severity: 'success', summary: 'Logged In', detail: 'Welcome!', life: 3000 });
      setTimeout(() => {
        router.push("/");
      }, 3000);
    } catch (err) {
      invalid.value = "p-invalid";
      show();
      setTimeout(() => {
        if (err.response.status == 401) {
          fadein.value = "fadeindown animation-duration-300"
          fadeout.value = "hidden"
          resend.value = true
          loginComponent.value = false
        }
      }, 1000);
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