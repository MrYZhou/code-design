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
          <el-form-item label="解析模式">
            <el-radio-group v-model="config.parseType" class="ml-4">
              <el-radio label="1" size="large">默认</el-radio>
              <!-- <el-radio label="2" size="large">目录</el-radio> -->
              <!-- <el-radio label="3" size="large">方案</el-radio> -->
              <el-radio label="4" :disabled="config.splitPanel" size="large">只预览</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="目录路径" v-if="config.parseType === '2'">
            <el-input v-model="config.templateDir" placeholder="请输入"></el-input>
          </el-form-item>
          <el-form-item label="服务地址">
            <el-input v-model="config.api" placeholder="请输入"></el-input>
          </el-form-item>
          <el-form-item label="数据映射">
            <el-input v-model="config.datakey" placeholder="请输入"></el-input>
          </el-form-item>
          <el-form-item label="隔离面板">
            <el-switch v-model="config.splitPanel" active-text="开" inactive-text="关" />
          </el-form-item>
          <el-form-item label="定时请求">
            <el-switch v-model="config.timeOpen" active-text="开" inactive-text="关" />
          </el-form-item>

          <el-form-item label="间隔" v-if="config.timeOpen">
            <el-input-number
              style="width: 100%"
              :step="1"
              :min="1"
              v-model="config.time"
              placeholder="请输入秒数"
            ></el-input-number>
          </el-form-item>
        </el-form>

        <el-row>
          <el-tag class="ml-2" type="success">数据库配置</el-tag>
        </el-row>

        <div class="mt10">
          <el-form
            :model="config.datbaseInfo"
            label-width="100px"
            :label-position="'left'"
          >
            <el-form-item label="连接地址">
              <el-input v-model="config.datbaseInfo.host" placeholder="请输入"></el-input>
            </el-form-item>
            <el-form-item label="连接端口">
              <el-input v-model="config.datbaseInfo.port" placeholder="请输入"></el-input>
            </el-form-item>

            <el-form-item label="用户名">
              <el-input v-model="config.datbaseInfo.user" placeholder="请输入"></el-input>
            </el-form-item>

            <el-form-item label="密码">
              <el-input
                v-model="config.datbaseInfo.password"
                placeholder="请输入"
              ></el-input>
            </el-form-item>

            <el-form-item label="过滤表前缀">
              <el-input
                v-model="config.datbaseInfo.prefix.table"
                placeholder="请输入"
              ></el-input>
            </el-form-item>

            <el-form-item label="过滤字段前缀">
              <el-input
                v-model="config.datbaseInfo.prefix.field"
                placeholder="请输入"
              ></el-input>
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
  api: "http://localhost:8000",
  parseType: "1",
  time: 1,
  datakey: "",
  templateDir: "",
  splitPanel: false,
  hasOne: false,
  timeOpen: false,
  vueType: "1",
  codeForm: "1",
  output: "",
  datbaseInfo: {
    host: "127.0.0.1",
    name: "study", // 数据库
    port: "3306",
    user: "root",
    password: "123456",
    prefix: {
      table: "la_",
      field: "f_",
    },
  },
});
const loadConfig = () => {
  let configData = localStorage.getItem("design-config");
  if (configData) {
    config = reactive({ ...JSON.parse(configData) });
  }
};
onMounted(() => {
  loadConfig();
});
const emit = defineEmits(["startDo","previewPanel"]);
function cancelClick() {
  drawer.value = false;
}
function confirmClick() {
  if(config.splitPanel && config.parseType == '4'){
    config.parseType = '1'
  }
  // 存pinia
  store.saveConfig(config);
  // 存localStorage
  localStorage.setItem("design-config", JSON.stringify(config));
  if(config.splitPanel){
    emit("previewPanel");
  }
  emit("startDo");
  cancelClick();
}
</script>
