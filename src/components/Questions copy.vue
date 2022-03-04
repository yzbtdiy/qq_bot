<script>

import axios from "axios"
import { reactive, onMounted } from "vue"
import router from '../router'


export default {

  setup ()
  {
    const state = reactive( {
      tabData: []
    } )
    onMounted( async () =>
    {
      const result = await axios.get( 'http://mybot.com/get_question' ).then( res => res.data )
      state.tabData = result
    } )
    return state
    function toAnswer(event){
       router.push( "/answer" )
    }
  }
}


</script>

<template>
  <el-table :data=" tabData " style="width: 100%" @row-click="toAnswer">
    <el-table-column prop="QUES_ID" label="问题ID" width="180" />
    <el-table-column prop="QUES_TXT" label="问题" />
  </el-table>
</template>

<style scoped>
</style>