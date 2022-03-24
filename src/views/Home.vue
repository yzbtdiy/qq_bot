<script setup>
import Header from '../components/Header.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <el-container>
    <el-header>
      <Header />
    </el-header>
    <el-main>
      <RouterView></RouterView>
    </el-main>
  </el-container>
</template>

<style lang="less">
html {
  height: 100%;
  body {
    height: 100%;
    margin: 0;
    #app {
      height: 100%;
      .el-container {
        height: 100%;
        .el-header {
          width: 100%;
        }
        .el-main {
          height: 100%;
        }
      }
    }
  }
}
</style>
