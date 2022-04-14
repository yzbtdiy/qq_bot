<script setup>
import request from "../utils/request"
import { reactive, onMounted, ref } from "vue"
import router from '../router'

const tabData = ref( [] )
const state = reactive( { tabData } )
const currentRow = ref()
// const singleTableRef = ref()
// const CancelCurrent = ( row ) =>
// {
//   singleTableRef.value.setCurrentRow( row )
// }

const handleCurrentChange = ( val ) =>
{
  currentRow.value = val
}


const reQue = ref( '' )

let questId = router.currentRoute.value.params.que_id


onMounted( async () =>
{
  const result = await request.get( '/get_answer/' + questId )
  state.tabData = result.data
} )


function useIt ()
{
  const answerId = currentRow.value.ANS_ID

  if ( currentRow && currentRow.value.IS_ADOPT == "None" )
  {
    currentRow.value.IS_ADOPT = "采用"
    request.put( '/update_question/' + questId + '/' + answerId )
    request.put( '/update_answer/' + answerId + '/' + '采用' )
  }

  router.go( 0 )
}

function reAsk ()
{
  const answerId = currentRow.value.ANS_ID
  const answerQq = currentRow.value.QQ_NUM
  const askTxt = reQue.value
  request.post( "/reask_question/", { answerId, answerQq, askTxt } )
}

</script>

<template>
  <div>
    <div>
      <el-input v-model=" reQue " placeholder="请选择答案, 再次提问" />
      <el-button @click=" useIt ">采用答案</el-button>
      <el-button @click=" reAsk ">后续提问</el-button>
      <!-- <el-button @click=" CancelCurrent ">取消选择</el-button> -->
    </div>
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
  </div>
</template>

<style scoped>
.el-button {
  margin-top: 16px;
}
</style>