<script setup>
import { ref, computed, onMounted } from 'vue'
import { Base64 } from "js-base64"
import Questions from './Questions.vue'




const ques = ref( '' )
const isPresent = computed( () => ques.value.length > 0 )

function submitQuest ()
{
  let addUrl = 'http://mybot.com/send_question/' + Base64.encode( ques.value )
  fetch( addUrl ).then( res => { return res } ).catch( err => { console.log( err ) } )
}
</script>

<template>
  <!-- <div>Hello, {{ name }}!</div> -->
  <el-input v-model=" ques " placeholder="请输入问题" />
  <el-button type="primary" :disabled=" !isPresent " @click=" submitQuest ">发布问题</el-button>
  <Questions></Questions>
</template>