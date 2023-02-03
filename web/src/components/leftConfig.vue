<template>
  <el-drawer v-model="drawer" :direction="direction">
    <template #header>
      <h4>配置面板</h4>
    </template>
    <template #default>
      <div>
        <el-form :model="config" label-width="100px" :label-position="'left'">
          <!-- <el-form-item label="版本">
            <el-radio-group v-model="config.vueType" class="ml-4">
              <el-radio label="1" size="large">vue2</el-radio>
              <el-radio label="2" size="large">vue3</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="平台">
            <el-radio-group v-model="config.codeForm" class="ml-4">
              <el-radio label="1" size="large">uniapp</el-radio>
              <el-radio label="2" size="large">web</el-radio>
            </el-radio-group>
          </el-form-item> -->
          <el-form-item label="解析类型">
            <el-radio-group v-model="config.parseType" class="ml-4">
              <el-radio label="1" size="large">默认</el-radio>
              <el-radio label="2" size="large">目录</el-radio>
              <el-radio label="3" size="large">方案</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="服务地址">
            <el-input v-model="config.api" placeholder="请输入"></el-input>
          </el-form-item>
        </el-form>

        <el-row>
          <el-tag class="ml-2" type="success">数据库配置</el-tag>
        </el-row>

        <div class="mt10">
          <el-form :model="datbaseInfo" label-width="100px" :label-position="'left'">
            <el-form-item label="连接地址">
              <el-input v-model="datbaseInfo.host" placeholder="请输入"></el-input>
            </el-form-item>
            <el-form-item label="连接端口">
              <el-input v-model="datbaseInfo.port" placeholder="请输入"></el-input>
            </el-form-item>

            <el-form-item label="用户名">
              <el-input v-model="datbaseInfo.user" placeholder="请输入"></el-input>
            </el-form-item>

            <el-form-item label="密码">
              <el-input v-model="datbaseInfo.password" placeholder="请输入"></el-input>
            </el-form-item>

            <el-form-item label="过滤表前缀">
              <el-input v-model="datbaseInfo.prefix.table" placeholder="请输入"></el-input>
            </el-form-item>

            <el-form-item label="过滤字段前缀">
              <el-input v-model="datbaseInfo.prefix.field" placeholder="请输入"></el-input>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </template>
    <template #footer>
      <div style="flex: auto">
        <el-button @click="cancelClick">关闭</el-button>
        <el-button type="primary" @click="confirmClick">确定</el-button>
      </div>
    </template>
  </el-drawer>
</template>

<script setup>
import { ElMessageBox } from "element-plus";
import { useMainStore } from "@/store";


const store = useMainStore();
const drawer = ref(false);
defineExpose({
  drawer,
});
const direction = ref("rtl");
let config = reactive({ 
  api:"http://localhost:8000",
  parseType:"1",
  vueType: "1", codeForm: "1", output: "" });
let datbaseInfo = reactive({
  host: "127.0.0.1",
  name: "study", // 数据库
  port: "3306",
  user: "root",
  password: "123456",
  prefix:{
    "table": "la_", "field": "f_" 
  }
});
function cancelClick() {
  drawer.value = false;
}
function showPanel() {
  drawer.value = true;
}
function confirmClick() {
   // 存在store
   store.saveConfig({...config,...datbaseInfo})
   drawer.value = false;
}
</script>
