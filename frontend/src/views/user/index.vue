<template>
    <h5>Help Text</h5>
    <div class="field" >
        <label for="username1" class="block text-900 font-medium mb-2">Username</label>
        <InputText id="username1" type="username" aria-describedby="username1-help" />
        <small id="username1-help">Enter your username to reset your password.</small>
    </div>
</template>
<script>
export default {

}
</script>

<style lang="scss" scoped>
.sizes {
    .p-inputtext {
        display: block;
        margin-bottom: .5rem;

        &:last-child {
            margin-bottom: 0;
        }
    }
}
.field * {
    display: block;
}
</style>