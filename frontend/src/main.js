import { createApp, reactive } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import Button from 'primevue/button';
import Card from 'primevue/card';
import Password from 'primevue/password';
import { createPinia } from 'pinia'
import 'primevue/resources/primevue.min.css';
import 'primeicons/primeicons.css';
import 'primeflex/primeflex.css';
// import 'primevue/resources/themes/tailwind-light/theme.css';
// import 'primevue/resources/themes/nano/theme.css';
import InputText from 'primevue/inputtext';
import { createI18n } from 'vue-i18n'
import messages from './helpers/locale/message.js'
import router from './router'
import DataTable from 'primevue/datatable';
import Toolbar from 'primevue/toolbar';
import ConfirmationService from 'primevue/confirmationservice';
import ToastService from 'primevue/toastservice';
let themeElement = document.getElementById('theme-link')
themeElement.setAttribute('href', 'node_modules/primevue/resources/themes/saga-blue/theme.css');

const pinia = createPinia()
const app = createApp(App);
const i18n = createI18n({
  locale: 'en', // set locale
  messages, // set locale messages
  legacy: false,
})
app.use(PrimeVue);
app.use(pinia);
app.use(i18n);
app.use(router);
app.use(ToastService);
app.component('Button', Button);
app.component('Card', Card);
app.component('InputText', InputText);
app.component('Password', Password);
app.component('Toolbar', Toolbar);
app.component('DataTable', DataTable);
app.use(ConfirmationService);
app.mount('#app');
