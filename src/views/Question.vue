<script setup>
import { ref, computed } from 'vue'
import { Base64 } from "js-base64"
const ques = ref( '' )
const isNamePresent = computed( () => ques.value.length > 0 )

function submitName ()
{
  let addUrl = 'http://mybot.com/send_question/' + Base64.encode( ques.value )
  fetch( addUrl ).then( res => { return res } ).catch( err => { console.log( err ) } )
}
</script>

<template>
  <!-- <div>Hello, {{ name }}!</div> -->
  <el-input v-model=" ques " placeholder="请输入问题" />
  <el-button type="primary" :disabled=" !isNamePresent " @click=" submitName ">Submit</el-button>
</template>