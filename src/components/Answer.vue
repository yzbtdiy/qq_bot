<script setup>
import request from "../utils/request"
import { reactive, onMounted, ref } from "vue"
import router from '../router'

const tabData = ref( [] )
const state = reactive( { tabData } )
const currentRow = ref()
const singleTableRef = ref()
const setCurrent = ( row ) =>
{
  singleTableRef.value.setCurrentRow( row )
}

const handleCurrentChange = ( val ) =>
{
  currentRow.value = val
}

let questId = router.currentRoute.value.params.ques_id


onMounted( async () =>
{
  const result = await request.get( '/get_answer/' + questId )
  state.tabData = result.data
} )


function useIt ()
{
  let answerId = currentRow.value.ANS_ID

  if ( currentRow && currentRow.value.IS_ADOPT == "未采用" )
  {
    currentRow.value.IS_ADOPT = "采用"
    request.put( '/update_question/' + questId + '/' + answerId )
    request.put( '/update_answer/' + answerId + '/' + '采用' )
  }

  router.go( 0 )
}

</script>

<template>
  <div>
    <el-table
      ref="singleTableRef"
      :data=" tabData "
      highlight-current-row
      style="width: 100%"
      @current-change=" handleCurrentChange "
    >
      <el-table-column prop="ANS_ID" label="答案ID" width="180" />
      <el-table-column prop="QQ_NUM" label="QQ号" width="180" />
      <el-table-column prop="ANS_TXT" label="答案" />
      <el-table-column prop="IS_ADOPT" label="状态" sortable width="120" fixed="right" />
    </el-table>
    <div style="margin-top: 20px">
      <el-button @click=" useIt ">采用答案</el-button>
      <el-button @click=" setCurrent() ">取消选择</el-button>
    </div>
  </div>
</template>

<style scoped>
</style>