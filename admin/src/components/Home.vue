<template>
  <div class="Home">
    <v-navigation-drawer fixed :clipped="$vuetify.breakpoint.width > 1264" app v-model="drawer">
      <v-list>
        <v-list-tile router to="/user">
          <v-list-tile-content>用户</v-list-tile-content>
        </v-list-tile>
        <v-list-tile router to="/semester">
          <v-list-tile-content>学期</v-list-tile-content>
        </v-list-tile>
        <v-list-tile router to="/course">
          <v-list-tile-content>课程</v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="primary" clipped-left fixedx app>
      <v-toolbar-title
        :style="$vuetify.breakpoint.width > 1264 && 'width: 100px'"
        class="ml-0 pl-3"
        :class="$vuetify.breakpoint.width <= 1264 && 'pr-3'">
        <v-toolbar-side-icon dark @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu v-model="menu">
        <v-btn color="orange" dark slot="activator">
          <v-icon left>account_circle</v-icon>
          {{ userID }}
        </v-btn>
        <v-card>
          <v-btn flat small color="red" @click="logout">注销</v-btn>
        </v-card>
      </v-menu>
    </v-toolbar>
    <v-content>
      <v-container fluid>
        <router-view name="body"></router-view>
      </v-container>
    </v-content>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    drawer: false,
    menu: false,
    userID: ''
  }),
  updated: function () {
    if (this.$cookie.get('id')) {
      this.userID = this.$cookie.get('id')
    }
  },
  methods: {
    logout: function () {
      this.$axios.get('logout/')
        .then(response => {
          this.$cookie.delete('id')
          this.userID = null
          this.$router.push('/login')
        })
        .catch(error => {
          console.log(error)
          this.$cookie.delete('id')
          this.userID = null
          this.$router.push('/login')
        })
    }
  }
}
</script>
