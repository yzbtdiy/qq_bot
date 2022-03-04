<script setup>
// import SideBar from '../components/Sidebar.vue'
import Header from '../components/Header.vue'
// import Answer from '../components/Main.vue'
import { RouterView } from 'vue-router'

</script>

<template>
  <el-container>
    <el-header>
      <Header />
    </el-header>
    <el-container>
      <!-- <el-aside>
        <SideBar />
      </el-aside>-->
      <el-main>
        <RouterView></RouterView>
        <!-- <Answer /> -->
      </el-main>
    </el-container>
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
        .el-container {
          height: 100%;
          // .el-aside {
          //   height: 100%;
          //   border-right: 1px solid #e6e6e6;
          // }
          .el-main {
            height: 100%;
          }
        }
      }
    }
  }
}
</style>
