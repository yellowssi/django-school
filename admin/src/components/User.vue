<template>
  <div class="User">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>用户管理</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="tab"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab>
          新建用户
        </v-tab>
        <v-tab>
          管理员
        </v-tab>
        <v-tab>
          教师
        </v-tab>
        <v-tab>
          学生
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        新建用户
      </v-tab-item>
      <v-tab-item>
        管理员
      </v-tab-item>
      <v-tab-item>
        教师
      </v-tab-item>
      <v-tab-item>
        学生
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'User',
  data: () => ({
    tab: null
  })
}
</script>

<style>
</style>
