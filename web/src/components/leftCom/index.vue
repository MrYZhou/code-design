<template>
  <div ref="editContainer" class="code-editor"></div>
</template>
<script setup>
import { getCurrentInstance, onMounted, watch } from "vue";
import * as monaco from "monaco-editor/esm/vs/editor/editor.main.js";
import JsonWorker from "monaco-editor/esm/vs/language/json/json.worker?worker";
let monacoEditor = null;
const { proxy } = getCurrentInstance();
// 解决vite Monaco提示错误
self.MonacoEnvironment = {
  getWorker() {
    return new JsonWorker();
  },
};
let props = defineProps({
  value: "",
});

const emit = defineEmits(["valueRefresh"]);
onMounted(() => {
  monacoEditor = monaco.editor.create(proxy.$refs.editContainer, {
    value: props.value,
    readOnly: false,
    language: "java",
    theme: "vs",
    selectOnLineNumbers: true,
    renderSideBySide: false,
  });
  // 监听值变化
  monacoEditor.onDidChangeModelContent(() => {
    const currenValue = monacoEditor?.getValue();
    emit('update:value', currenValue);
    emit("valueRefresh", currenValue);
  });
});

</script>
<style scoped>
.code-editor {
  width: 100%;
  height: 100%;
  bottom: 1px solid red;
}
</style>
