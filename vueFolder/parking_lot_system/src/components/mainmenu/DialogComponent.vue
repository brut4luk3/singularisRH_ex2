<template>
    <div v-if="visible" class="overlay">
      <div class="dialog">
        <button class="close-btn" @click="closeDialog">X</button>
        <slot></slot>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['visible'],
    methods: {
      closeDialog() {
        this.$emit('close');
      }
    }
  }
  </script>
  
  <style src="./globalFormStyle.css" scoped></style>  