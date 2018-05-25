<template>
  <div class="User">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-toolbar-title>用户管理</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="model"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab
          v-for="i in 3"
          :key="i"
          :href="`#tab-${i}`"
        >
          Item {{ i }}
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="model">
      <v-tab-item
        v-for="i in 3"
        :key="i"
        :id="`tab-${i}`"
      >
        <v-card flat>
          <v-card-text v-text="text"></v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'User'
}
</script>

<style>
</style>
