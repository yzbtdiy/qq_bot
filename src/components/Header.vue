<script setup>
import { ref } from 'vue'
import { routerKey } from 'vue-router'
import router from '../router'

const activeIndex = ref( '1' )
const activeIndex2 = ref( '1' )
const handleSelect = ( key, keyPath ) =>
{
  // console.log( key, keyPath )
}

function toAnswer ()
{
  router.push( "/answer" )
}
function toQuestion ()
{
  router.push( "/question" )
}
</script>

<template>
  <el-menu
    :default-active=" activeIndex "
    class="el-menu-demo"
    mode="horizontal"
    @select=" handleSelect "
  >
    <div class="title">QQBot问答管理</div>

    <el-menu-item index="1" @click=" toQuestion ">问题处理</el-menu-item>
    <!-- <el-menu-item index="2" @click=" toAnswer ">答案收集</el-menu-item> -->
    <!-- <el-sub-menu index="2">
      <template #title>Workspace</template>
      <el-menu-item index="2-1">item one</el-menu-item>
      <el-menu-item index="2-2">item two</el-menu-item>
      <el-menu-item index="2-3">item three</el-menu-item>
      <el-sub-menu index="2-4">
        <template #title>item four</template>
        <el-menu-item index="2-4-1">item one</el-menu-item>
        <el-menu-item index="2-4-2">item two</el-menu-item>
        <el-menu-item index="2-4-3">item three</el-menu-item>
      </el-sub-menu>
    </el-sub-menu> 
    <el-menu-item index="3" disabled>Info</el-menu-item>-->
    <!-- <router-link to="/question"><el-menu-item index="2">添加问题</el-menu-item></router-link> -->
  </el-menu>
</template>

<style scoped>
.title {
  margin: auto 10vh;
}
</style>