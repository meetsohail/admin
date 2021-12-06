<template>
    <div class="alert" :class="clsname">
        {{ msg }}
    </div>
</template>
<script>
export default {
    props: ['msg', 'clsname']
}
</script>