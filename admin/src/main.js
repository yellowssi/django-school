// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import VueCookie from 'vue-cookie'
import Axios from 'axios'
import App from './App'
import router from './router'
import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

Vue.config.productionTip = true

Vue.use(Vuetify)

Vue.prototype.$axios = Axios.create({
  baseURL: 'http://admin.yellowsea.top/api/',
  headers: {'Content-Type': 'Application/json;charset=utf-8'},
  withCredentials: true,
  timeout: 5000
})

Vue.prototype.$cookie = VueCookie

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
