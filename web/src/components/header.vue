<script setup>
import { useMainStore } from "@/store";

import { View, Tools, Download } from "@element-plus/icons-vue";

const store = useMainStore();
const input = ref("");
</script>

<template>
  <div class="wrap" >
    <div class="search-btn">
      <el-input v-model="input" placeholder="输入文件名"/>
    </div>
  </div>
</template>

<style scoped type="scss">
.wrap {
  margin-top: 20px;
  height: 100%;
}
.search-btn {
  margin:auto;
  width: 38%;
}
</style>
