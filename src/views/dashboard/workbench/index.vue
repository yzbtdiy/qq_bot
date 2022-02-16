<template>
  <PageWrapper>
    <div>
      <a-textarea
        v-model:value=" value1 "
        placeholder="Autosize height based on content lines"
        auto-size
      />
      <!-- <div style="margin: 24px 0" />
    <a-textarea
      v-model:value="value2"
      placeholder="Autosize height with minimum and maximum number of lines"
      :auto-size="{ minRows: 2, maxRows: 5 }"
      />-->
    </div>
    <!-- <template #headerContent> <WorkbenchHeader /> </template>
    <div class="lg:flex">
      <div class="lg:w-7/10 w-full !mr-4 enter-y">
        <ProjectCard :loading="loading" class="enter-y" />
        <DynamicInfo :loading="loading" class="!my-4 enter-y" />
      </div>
      <div class="lg:w-3/10 w-full enter-y">
        <QuickNav :loading="loading" class="enter-y" />

        <Card class="!my-4 enter-y" :loading="loading">
          <img class="xl:h-50 h-30 mx-auto" src="../../../assets/svg/illustration.svg" />
        </Card>

        <SaleRadar :loading="loading" class="enter-y" />
      </div>
    </div>-->
  </PageWrapper>
</template>
<script lang="ts" setup>
import { Card } from 'ant-design-vue'
import { PageWrapper } from '/@/components/Page'
import WorkbenchHeader from './components/WorkbenchHeader.vue'
import ProjectCard from './components/ProjectCard.vue'
import QuickNav from './components/QuickNav.vue'
import DynamicInfo from './components/DynamicInfo.vue'
import SaleRadar from './components/SaleRadar.vue'

import { defineComponent, ref } from 'vue'
//

// const loading = ref( true )

// setTimeout( () =>
// {
//   loading.value = false
// }, 1500 )
</script>
