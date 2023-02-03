<template>
  <!-- 抽屉面板 -->
  <leftConfig ref="leftconfig"></leftConfig>
  <jsonDrawer ref="jsondrawer" @valueRefresh="parse"></jsonDrawer>
  <!-- 主布局 -->
  
  <div class="larry">
    <div class="group group-show">
      <leftCom v-model:value="data.value1" @valueRefresh="parse"></leftCom>
    </div>
    <div class="btn-group">
      <div><el-button @click="doConfig" :icon="Tools"></el-button></div>
      <div><el-button @click="doView" :icon="View"></el-button></div>
      <div><el-button @click="doDownload" :icon="Download"></el-button></div>
      <div><el-button @click="jsonData" :icon="Document"></el-button></div>
    </div>
    <div class="group group-form">
      <rightCom v-model:value="data.value2"></rightCom>
    </div>
  </div>
</template>
<script  setup>
import rightCom from "./rightCom/index.vue";
import leftCom from "./leftCom/index.vue";
import { View, Tools, Download,Document } from "@element-plus/icons-vue";
import { useMainStore } from "@/store";
import { ElMessageBox } from "element-plus";

const store = useMainStore();
let data = reactive({value2:'',value1:''})
onMounted(() => {

  // setInterval(()=>{
  //   parse()
  // },1000 * 2)
});
const axios = inject('axios')  // inject axios

// 显示控制面板
const leftconfig = ref();
const doConfig = () => {
  leftconfig.value.drawer = true;
};

// 数据填充,这里很坑啊,ref必须先获取才能调
const jsondrawer = ref();
const jsonData = () => {
  jsondrawer.value.drawer = true;
};

const valueChange1 = (data) => {
  data.value1=data
};
//预览
const doView = async () => {
  if(data.value1.length==0){
    ElMessage({
      message: '没有要解析的字符',
      type: 'warning',
    })
    return
  }
  parse()
  
};

const parse =async ()=>{
  if(data.value1.length==0) return 
  let info  = {content:data.value1,...store.config,configData:store.renderData}
  let res = await axios.post('http://localhost:8000/generate/codeParse',info)
  data.value2 = res.data
}


// 下载
const doDownload = () => {
};



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
.btn-group{
  margin:0 5px;
  padding: 2px;
}
.btn-group div{
  margin-bottom: 5px;
}
.group {
  border: 1px solid #51c4d3;
  padding: 12px 0px;
  width: 48%;
  background-color: #fff;
  /* overflow-y: scroll; */
  overflow-y: hidden;
}

.group-form {
  
}
.group-form::-webkit-scrollbar {
  display: none;
}
.group-show {
  /* margin-right: 10px; */
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
