<template>
  <div class="login-body">
    <div class="login-wrapper">
        <div class="login-panel">
          <div>logo</div>
          <div class="login-form">
            <h2>Create Your Free Account</h2>
            <p>Already have an account? <a href="#/" class="">Login</a></p>
            <div class="p-inputgroup mb-4">
              <span class="p-inputgroup-addon">
                  <i class="pi pi-user"></i>
              </span>
              <InputText v-model="email" />
            </div> 
      
            <div class="p-inputgroup mb-4">
              <span class="p-inputgroup-addon">
                  <i class="pi pi-key"></i>
              </span>
              <Password v-model="password" />
            </div> 
            <Checkbox v-model="checked" :binary="true"  name="city" value="Chicago"/>
            <Button label="Sign In" icon="pi pi-user" class="w-full" @click="changeTheme($event.target.value)"></Button>
          </div>
          <p>A problem? <a href="#/" class="">Click here</a> and let us help you.</p>
        </div>
        <div class="login-image">
          {{password}}
        </div>
    </div>
  </div> 
</template>

<script>
import Checkbox from 'primevue/checkbox';

export default {
  components: { Checkbox },
  data() {
    return {
      email: "",
      password: "",
      checked: false,
    };
  },
  computed: {},
  methods:{
    changeTheme(event) {
      let themeElement = document.getElementById('theme-link')
      themeElement.setAttribute('href', 'node_modules/primevue/resources/themes/mdc-dark-indigo/theme.css');
}
  },
};
</script>

<style scoped>
  .login-body {
    background: var(--surface-card);
    color: var(--text-color);
}
  .login-body .login-wrapper {
    display: flex;
    height: 100vh;
}
.login-body .login-wrapper .login-panel {
  width: 30%;
  height: 100%;
  text-align: center;
  padding: 40px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
}
@media (min-width: 993px){
.login-body .login-wrapper .login-image {
    background-size: cover;
    background-repeat: no-repeat;
    background-image: url('https://www.primefaces.org/diamond-vue/layout/images/pages/bg-login.jpg');
}
}
.login-body .login-wrapper .login-image {
  width: 70%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
  padding: 40px 20px;
}
.login-panel {
  width: 30%;
  height: 100%;
  text-align: center;
  padding: 40px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
}
.login-form {
  display: flex;
  align-items: center;
  flex-direction: column;
}
</style>
