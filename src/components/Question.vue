<script setup>
import request from '../utils/request'
import { reactive, onMounted, computed, ref } from "vue"
import router from '../router'
import { Base64 } from "js-base64"
import HisQuestVue from './HisQuest.vue'

const ques = ref( '' )
const isPresent = computed( () => ques.value.length > 0 )

const tabData = ref( [] )
const state = reactive( { tabData } )

async function submitQuest ()
{
  let quest = String( Base64.encode( ques.value ) )
  await request.post( '/send_question', { question: quest } )
  ques.value = ""
}


onMounted( async () =>
{
  const result = await request.get( '/get_question' )
  state.tabData = result.data
} )


function toAnswer ( event )
{
  router.push( { name: "Answer", params: { ques_id: event.QUES_ID } } )
}


</script>

<template>
  <el-input v-model=" ques " placeholder="请输入问题" />
  <el-button type="primary" :disabled=" !isPresent " @click=" submitQuest ">发布问题</el-button>
  <HisQuestVue />
  <el-table :data=" tabData " style="width: 100%" @row-click=" toAnswer ">
    <el-table-column prop="QUES_ID" label="问题ID" width="180" />
    <el-table-column prop="QUES_TXT" label="问题" />
    <el-table-column prop="ADOPT_ANS" label="采纳答案" />
  </el-table>
</template>

<style scoped>
.el-button {
  margin-top: 12px;
}
</style>