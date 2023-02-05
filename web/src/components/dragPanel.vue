<template>
  <!-- 抽屉面板 -->
  <config ref="configPanel" @startDo="startDo"></config>
  <jsonDrawer ref="jsondrawer" @valueRefresh="parse"></jsonDrawer>
  <!-- 主布局 -->
  <div class="larry">
    <div
      class="group group-show"
      :style="splitState ? 'width: 100%;' : 'width: 48%;'"
      v-if="!isPreview && store.config.parseType != 4"
    >
      <leftCom ref="leftcom" v-model:value="data.value1" @valueRefresh="parse"></leftCom>
    </div>
    <div class="btn-group" v-if="!isPreview">
      <div><el-button @click="doConfig" :icon="Tools"></el-button></div>
      <template v-if="store.config.parseType != 4">
        <div><el-button @click="doParse" :icon="View"></el-button></div>
        <!-- <div><el-button @click="doDownload" :icon="Download"></el-button></div> -->
        <div><el-button @click="previewPanel" :icon="DocumentCopy"></el-button></div>
      </template>

      <div><el-button @click="jsonData" :icon="Dish"></el-button></div>
    </div>
    <div
      class="group group-form"
      :style="splitState || store.config.parseType == 4 ? 'width: 100%;' : 'width: 48%;'"
      v-if="!splitState || isPreview"
    >
      <rightCom ref="rightcom" v-model:value="data.value2"></rightCom>
    </div>
  </div>
</template>
<script setup>
import rightCom from "./rightCom/index.vue";
import leftCom from "./leftCom/index.vue";
import {
  View,
  Tools,
  Download,
  Document,
  DocumentCopy,
  Dish,
} from "@element-plus/icons-vue";
import { useMainStore } from "@/store";
import { ElMessageBox } from "element-plus";

const store = useMainStore();
let data = reactive({ value2: "", value1: "" });
let timer = ref("");

const startDo = () => {
  let config = store.config;
  clearInterval(timer);
  if (config.timeOpen) {
    timer = setInterval(() => {
      parse();
    }, 1000 * config.time);
  }
  if (config.splitPanel) {
    previewPanel();
  }
};

let splitState = ref(false);
let subWindow = ref(null);
let rightcom = ref();
let leftcom = ref();
const previewPanel = () => {
  subWindow = window.open(window, "preview", { target: "_blank" });
  splitState.value = true;
  rightcom.value.show = false;
};

const postMessage = (msg) => {
  subWindow.postMessage({ type: "preview", msg }, "/");
};

const initListener = () => {
  window.addEventListener("message", function (event) {
    if (event.data?.type != "preview") {
      return;
    }
    data.value2 = event.data.msg;
  });
};

// 显示控制面板
const configPanel = ref();
let isPreview = ref(false);
watchEffect(() => {});
onMounted(() => {
  startDo();

  initListener();

  if (window.name === "preview") {
    isPreview = true;
    splitState.value = true;
    leftcom.value.hide();
  }
});
const axios = inject("axios"); // inject axios

const doConfig = () => {
  configPanel.value.drawer = true;
};

// 数据填充,这里很坑啊,ref必须先获取才能调
const jsondrawer = ref();
const jsonData = () => {
  jsondrawer.value.drawer = true;
};

const valueChange1 = (data) => {
  data.value1 = data;
};

const doParse = async () => {
  if (data.value1.length == 0) {
    ElMessage({
      message: "没有要解析的字符",
      type: "warning",
    });
    return;
  }
  parse();
};

const parse = async () => {
  let config = store.config;
  if (data.value1.length == 0) return;
  let info = { content: data.value1, ...store.config, configData: store.renderData };
  let res = await axios.post(`http://127.0.0.1:8000/generate/codeParse`, info);

  if (config.datakey) {
    let keyList = config.datakey.split(".");
    keyList.forEach((key) => {
      if (res.data.hasOwnProperty(key)) {
        res.data = res.data[key];
      }
    });
  }
  let value = res.data;
  if (typeof value === "string") {
    data.value2 = value;
    if (splitState) {
      postMessage(value);
    }
  }
};

// 下载
const doDownload = () => {};
</script>
<style type="scss">
.larry {
  background-color: #f1f1f1;
  display: flex;
  justify-content: space-between;
  min-width: 990px;
  height: calc(100vh - 50px);
  overflow-y: hidden;
}
.larry::-webkit-scrollbar {
  display: none;
}
.wrap-form {
  display: inline-block;
}
.btn-group {
  margin: 0 5px;
  padding: 2px;
}
.btn-group div {
  margin-bottom: 5px;
}
.group {
  border: 1px solid #51c4d3;
  padding: 12px 0px;
  background-color: #fff;
  /* overflow-y: scroll; */
  overflow-y: hidden;
}

/* .group-form {
}
.group-show {
} */
.group-form::-webkit-scrollbar {
  display: none;
}

.group-show::-webkit-scrollbar {
  display: none;
}

.config-info {
  border: 1px solid red;
  margin: 20px;
  padding: 20px;
  height: 30vh;
}
.delete-icon {
  position: absolute;
  /* width: 24px; */
  font-size: 22px;
  padding: 10px;
  /* background-color: aliceblue; */
  right: 6px;
  /* right: -39px; */
  top: -16px;
  z-index: 9999;
  border-radius: 50%;
  /* border: 1px solid #ccc; */
  /* border: 1px solid red; */
}
.delete-icon:hover {
  color: rgb(206, 103, 103);
  background-color: #f1f1f1;
}
.item {
  border: solid 1px #ddd;
  padding: 0px;
  text-align: left;
  background-color: #fff;
  display: flex;
  align-items: center;
  height: 36px;
  /* line-height: 38px; */
  /* user-select: none; */
}
.item-control {
  display: inline-block;
  width: 100px;
  height: 45px;
  line-height: 45px;
  margin: 3px;
  text-align: center;
}

.item > label {
  padding: 6px 10px;
  color: #333;
}
.item > label:hover {
  cursor: move;
}
.item > span {
  padding: 6px 10px;
  color: #666;
}
.ghost {
  border: solid 1px pink !important;
}
.chosenClass {
  opacity: 1;
  border: solid 1px #ccc;
}
.fallbackClass {
  background-color: aquamarine;
}
</style>
