<script setup>
// import { reqAnswers } from "../api"

// let res = reqAnswers('tsatatatat')
// console.log(res)
// let data = ( await axios.get( 'http://127.0.0.1:5000/get_answer' ) ).data
// let tabdata=JSON.stringify(data)

import axios from "axios"
import { reactive, onMounted, ref } from "vue"
import router from '../router'

const tabData = ref( [] )
const state = reactive( { tabData } )

let quesId = router.currentRoute.value.params.ques_id

onMounted( async () =>
{
  const result = await axios.get( 'http://mybot.com/get_answer/' + quesId ).then( res => res.data )
  state.tabData = result
} )


</script>

<template>
  <el-table :data=" tabData " style="width: 100%">
    <el-table-column prop="QUES_ID" label="问题ID" width="180" />
    <el-table-column prop="QQ_NUM" label="QQ号" width="180" />
    <el-table-column prop="USER_CON" label="答案" />
  </el-table>
</template>

<style scoped>
</style>