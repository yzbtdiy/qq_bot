<script setup>
import { reactive, onMounted, ref } from "vue"
import request from "../utils/request"
const tabData = ref( [] )
const state = reactive( { tabData } )

onMounted( async () =>
{
  const result = await request.get( '/get_recent_quest/' )
  state.tabData = result.data
} )

</script>

<template>
  <el-dropdown>
    <span class="el-dropdown-link">
      问题追踪
      <el-icon class="el-icon--right">
        <arrow-down />
      </el-icon>
    </span>
    <template #dropdown>
      <el-dropdown-menu>
        <el-dropdown-item>Action 1</el-dropdown-item>
        <el-dropdown-item>Action 2</el-dropdown-item>
        <el-dropdown-item>Action 3</el-dropdown-item>
        <el-dropdown-item disabled>Action 4</el-dropdown-item>
        <el-dropdown-item divided>Action 5</el-dropdown-item>
      </el-dropdown-menu>
    </template>
  </el-dropdown>
</template>

<style scoped>
.el-dropdown {
  margin-top: 20px;
  margin-left: 20px;
}
</style>