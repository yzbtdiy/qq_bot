<script setup>
import { ref } from 'vue'

defineProps( {
  msg: String
} )

const count = ref( 0 )
</script>

<template>
  <div class="login-container">
    <el-form>
      <el-form-item label="用户">
        <el-input></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input></el-input>
      </el-form-item>
      <el-form-item class="button">
        <el-button id="submit">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<style scoped lang="less">
.login-container {
  display: flex;
  justify-content: center;
  margin-top: 40vh;
  // align-items: center;
  #submit {
    margin-top: 18px;
    position: absolute;
    margin-left: 50%;
    left: -16px;
  }
}
</style>
