<template>
    <span>
        <span v-if="busy">
            <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> {{ bText }}
        </span>
        <span v-else>{{ nText }}</span>
    </span>
</template>
<script>
export default {
    props: {
        busy: {
            default: false,
            type: Boolean
        },
        bText: {
            default: 'Working',
            type: String
        },
        nText: {
            default: 'Update',
            type: String
        }
    }
}
</script>