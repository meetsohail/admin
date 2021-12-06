<template>
<div>
<button class="float-right border rounded p-1" @click="$store.commit('setUser')"
                    >Credits: {{ $store.state.user.credit | toNumber }}</button
                >
</div>
</template>
<script>
</script>