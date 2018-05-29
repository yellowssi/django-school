<template>
  <div class="Course">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>课程管理</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="tab"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab>
          课程列表
        </v-tab>
        <v-tab>
          新增课程
        </v-tab>
        <v-tab>
          各学期课程
        </v-tab>
        <v-tab>
          新增学期课程安排
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        课程列表
      </v-tab-item>
      <v-tab-item>
        新增课程
      </v-tab-item>
      <v-tab-item>
        各学期课程
      </v-tab-item>
      <v-tab-item>
        新增学期课程安排
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Course',
  data: () => ({
    tab: null
  })
}
</script>
