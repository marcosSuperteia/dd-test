<template>
  <div class="card">
    <Toolbar class="mb-4 indigo-400">
        <template #start>
            <Button :label="$t('message.new')" icon="pi pi-plus" class="p-button mr-2" @click="openEditDialog"/>          
        </template>      
    </Toolbar>
    <DataTable
      :value="roles"
      class="p-datatable-lg"
      responsiveLayout="scroll"
      @rowSelect="onRowSelect"
      selectionMode="single"
      dataKey="id"
      v-model:selection="selectedItemTable" 
    >
      <Column field="id" header="ID" hidden></Column>
     <Column field="name" :sortable="true" :header="$t('message.name', { msg: 'Name' })"></Column>
      <Column field="description" :sortable="true" :header="$t('message.description', { msg: 'Description' })"></Column>
      <Column
        headerStyle="text-align: right"
        bodyStyle="text-align: right; overflow: visible"
        :exportable="false"
      >
        <template #body="slotProps">
          <Button
            icon="pi pi-pencil"
            class="p-button-rounded p-button-success mr-2"
            @click="openEditDialog(slotProps.data)"
          />
          <Button
            icon="pi pi-trash"
            class="p-button-rounded p-button-warning"
            @click="deleteRole(slotProps.data)"
          />
        </template>
      </Column>
    </DataTable>
    <Dialog
      v-model:visible="display"
      :style="{ width: '650px' }"
      header="Product Details"
      :modal="true"
      class="p-fluid"
    >
      <div class="field">
        <div class="p-inputgroup mb-5">
          <MultiSelect v-model="selectedCars" :options="permissions" optionLabel="name" placeholder="Select Brands" />
          <Button label="adicionar" class="p-button-success" @click="addPermission()"/>
        </div>  
        <DataTable
        style="max-height:400px"
        :value="selectedItemTable.role_permission"
        class="p-datatable-lg"
        :scrollable="true" scrollHeight="flex"
      >
      <Column field="id" header="ID" :sortable="true" hidden></Column>
      <Column field="permission.name" header="Nome"></Column>
      <Column field="permission.description" header="Description"></Column>
    </DataTable> 
      </div>
      <template #footer>
        <Button
          label="No"
          icon="pi pi-times"
          @click="closeDialogPermission"
          class="p-button-text"
        />
        <Button label="Yes" icon="pi pi-check" @click="updatePermission()" autofocus />
      </template>
    </Dialog>
    <Dialog v-model:visible="displayForm" :style="{width: '450px'}" :header="!selectedId ? $t('new_dialog.header_permission_save'): $t('new_dialog.header_permission_edited')" :modal="true" class="p-fluid">
      <FormRole @sendRole="editRole"></FormRole>
    </Dialog>
    <ConfirmDialog group="templating"/>
    <Toast />
  </div>
</template>
<script setup>
import axios from "axios";
import Column from "primevue/column";
import Dialog from "primevue/dialog";
import MultiSelect from 'primevue/multiselect';
import { ref, onMounted  } from "vue";
import { useToast } from "primevue/usetoast";
import Toast from 'primevue/toast';
import ConfirmDialog from 'primevue/confirmdialog';
import { useConfirm } from "primevue/useconfirm";
import { useI18n } from 'vue-i18n'
import FormRole from './form-role/index.vue';
const { t } = useI18n({})
const confirm = useConfirm();
const toast = useToast();
const roles = ref([]);
const selectedItemTable = ref([]);
const selectedCars = ref([]);
const display = ref(false);
const displayForm = ref(false);
const permissions = ref([])
const selectedId = ref(false);

// Api methods
const getRoles = async () => {
    const response = await axios.get("http://localhost:8000/api/v1/roles");
    roles.value = response.data;
    console.log(`the component is now mounted.`, response.data)
}
const getPermission = async () => {
  const response = await axios.get("http://localhost:8000/api/v1/permissions")
  permissions.value = response.data;
}
const updatePermission = async() => {
  const response = await axios.put("http://localhost:8000/api/v1/role_permissions/"+selectedItemTable.value.id, selectedCars.value); 
  
  if(response.status == 200){
    toast.add({severity:'success', summary: 'Atualizado conforme solicitado', detail:'Permissoes atualizadas para a regra', life: 3000});
  }   
  display.value = false;
};

const onRowSelect = (event)=> {
    var permissions = [] 
    selectedItemTable.value.role_permission.forEach(el => {
      permissions.push(el.permission)
    })
    selectedCars.value = permissions
    display.value = true;
}

const closeDialogPermission = () => {
  console.log("true");
  display.value = false;
};
const openEditDialog = (data) => {
  selectedId.value = data.id
  console.log("true")
  displayForm.value = true;
};
const deleteRole = async (data) => {
  selectedId.value = data.id
  confirm.require({
    group: 'templating',
                header:  t('delete_dialog.header'),
                message: t('delete_dialog.message'),
                icon: 'pi pi-question-circle',
                acceptLabel:t('delete_dialog.yes'), 
                rejectLabel:t('delete_dialog.no'), 
                acceptIcon: 'pi pi-check',
                rejectIcon: 'pi pi-times',
            accept: async () => {
              const response = await axios.delete("http://localhost:8000/api/v1/roles/"+selectedId.value);              
              toast.add({severity:'warn', summary: t('delete_dialog.header'), detail:t('delete_dialog.message_sucess'), life: 3000});
              getRoles();
              getPermission();
            }
        });
};
const editRole = async(data) => {
    console.log(selectedId)
    if (!selectedId.value) {
      const response = await axios.post("http://localhost:8000/api/v1/roles/",{name:data.v$.value.name.$model, description: data.v$.value.description.$model});              
      toast.add({severity:'success', summary:t('new_dialog.header_permission_save'), detail:t('new_dialog.message_permission_save_sucess'), life: 3000});
      getRoles();
      getPermission();
    } else {
      if(!data.v$.value.$invalid){
        const response = await axios.put("http://localhost:8000/api/v1/roles/"+selectedId.value,{name:data.v$.value.name.$model, description: data.v$.value.description.$model});              
        toast.add({severity:'success', summary: t('new_dialog.header_permission_edited'), detail:t('new_dialog.message_permission_edited_sucess'), life: 3000});
        getRoles();
        getPermission();
    }
    }
    
    displayForm.value = false;
}
const addPermission = () => {
  console.log(selectedItemTable.value.role_permission)
 selectedItemTable.value.role_permission = []
var permission = []
 selectedCars.value.forEach(el => {
    permission.push({'permission' : el})
 })
 selectedItemTable.value.role_permission = permission
 console.log(selectedItemTable.value.role_permission)
};
onMounted(() => {
  getRoles();
  getPermission();
})
</script>
<style>
@import "./style.css";
</style>
