<template>
  <el-drawer v-model="drawer" :direction="direction" size="48%">
    <template #header>
      <h4>json数据配置</h4>
    </template>
    <template #default>
      <div>
        <el-input
          v-model="textarea1"
          type="textarea"
          placeholder=""
        />
        <!-- <json-viewer v-model:value="parseValue" copyable sort></json-viewer> -->
      </div>
    </template>
    <template #footer>
      <div style="flex: auto">
        <el-button @click="cancelClick">取消</el-button>
        <el-button type="primary" @click="confirmClick">确定</el-button>
      </div>
    </template>
  </el-drawer>
</template>

<script  setup>
import { ref } from 'vue'
import { ElMessageBox } from 'element-plus'
import { useMainStore } from "@/store";

const store = useMainStore();
let textarea1  = ref('')
const drawer = ref(false)
const direction = ref('ltr')
defineExpose({
  drawer,
});
function cancelClick() {
  drawer.value = false
}
const emit = defineEmits(['valueRefresh'])
function confirmClick() {
  store.configData(textarea1)
  emit('valueRefresh','')
  drawer.value = false
}
</script>
<style scope>
  .el-textarea__inner{
    height: calc(100vh - 150px);
  }
  .el-drawer__header{
    margin-bottom: 0;
  }
</style>
