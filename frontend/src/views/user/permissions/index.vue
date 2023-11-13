<template>
  
  <div class="card">
    <Toolbar class="mb-4 indigo-400">
        <template #start>
            <Button :label="$t('message.new')" icon="pi pi-plus" class="p-button mr-2" @click="openDialog"/>          
        </template>      
    </Toolbar>
    <DataTable :value="permissions" class="p-datatable-lg" responsiveLayout="scroll" dataKey="id">
      <Column field="id" header="ID" hidden></Column>
      <Column field="name" :sortable="true" :header="$t('message.name')"></Column>
      <Column field="description" :sortable="true" :header="$t('message.description')"></Column>
      <Column headerStyle="text-align: right" bodyStyle="text-align: right; overflow: visible">
        <template #body="slotProps">
          <Button icon="pi pi-pencil" class="p-button-rounded p-button-success mr-2" @click="openDialog(slotProps.data)"/>
          <Button icon="pi pi-trash" @click="deletePermission(slotProps.data)" class="p-button-rounded p-button-warning" />
        </template>
      </Column>
    </DataTable>
    <ConfirmDialog group="templating"/>
    <Toast />
    <Dialog v-model:visible="display" :style="{width: '450px'}" :header="!selectedId ? $t('new_dialog.header_permission_save'): $t('new_dialog.header_permission_edited')" :modal="true" class="p-fluid">
      <FormPermission @sendPermission="editPermission"></FormPermission>
  </Dialog>
  </div>
</template>
<script setup>
import axios from "axios";
import Column from "primevue/column";
import { ref, onMounted } from "vue";
import ConfirmDialog from 'primevue/confirmdialog';
import { useConfirm } from "primevue/useconfirm";
import { useI18n } from 'vue-i18n'
import { useToast } from "primevue/usetoast";
import Toast from 'primevue/toast';
import Dialog from 'primevue/dialog';
import FormPermission from './form-permission/index.vue';
const { t } = useI18n({})
const display = ref(false);
const permissions = ref([]);
const confirm = useConfirm();
const toast = useToast();
const selectedId = ref(false);

const getPermission = async () => {
  const response = await axios.get("http://localhost:8000/api/v1/permissions"); 
  permissions.value = response.data;
  selectedId.value = false;
};
const editPermission = async(data) => {
    console.log(selectedId)
    if (!selectedId.value) {
      const response = await axios.post("http://localhost:8000/api/v1/permissions/",{name:data.v$.value.name.$model, description: data.v$.value.description.$model});              
      toast.add({severity:'success', summary:t('new_dialog.header_permission_save'), detail:t('new_dialog.message_permission_save_sucess'), life: 3000});
      getPermission();
    } else {
      if(!data.v$.value.$invalid){
        const response = await axios.put("http://localhost:8000/api/v1/permissions/"+selectedId.value,{name:data.v$.value.name.$model, description: data.v$.value.description.$model});              
        toast.add({severity:'success', summary: t('new_dialog.header_permission_edited'), detail:t('new_dialog.message_permission_edited_sucess'), life: 3000});
        getPermission();
    }
    }
    
    display.value = false;
}
onMounted(() => {
});
const deletePermission = async (data) => {
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
              const response = await axios.delete("http://localhost:8000/api/v1/permissions/"+selectedId.value);              
              toast.add({severity:'warn', summary: t('delete_dialog.header'), detail:t('delete_dialog.message_sucess'), life: 3000});
              getPermission();
            }
        });
};
const openDialog = (data) => {
        selectedId.value = data.id
        console.log("true")
        display.value = true;
};

</script>
<style>
@import "./style.css";
</style>
