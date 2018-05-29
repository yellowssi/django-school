<template>
  <div class="Semester">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>学期管理</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="tab"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab>
          学期选课开通
        </v-tab>
        <v-tab>
          新增学期
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-data-table
          :headers="headers"
          :items="semesters"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.year }}</td>
            <td>{{ props.item.season }}</td>
            <td>{{ props.item.start_date }}</td>
            <td>{{ props.item.end_date }}</td>
            <td>{{ props.item.status ? '已开通' : '未开通' }}</td>
            <td>
              <v-btn icon @click="openSemesterCourse(props.item.id)" :disabled="props.item.status">
                <v-icon color="success">done</v-icon>
              </v-btn>
              <v-btn icon @click="closeSemesterCourse(props.item.id)" :disabled="!props.item.status">
                <v-icon color="error">clear</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <br/>
        <v-form ref="semesterForm" v-model="newSemester.valid" lazy-validation>
          <v-text-field
            label="学年"
            v-model="newSemester.year"
            :rules="newSemester.yearRules"
            hint="格式:17-18"
            required></v-text-field>
          <v-divider></v-divider>
          <br/>
          <h3>秋季学期</h3>
          <v-layout row wrap>
            <v-flex xs6>
              <v-menu
                ref="menu1"
                :close-on-content-click="false"
                v-model="newSemester.autumn.startMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.autumn.startDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.autumn.startDate"
                  label="开始日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.autumn.startDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.autumn.startMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu1.save(newSemester.autumn.startDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs6>
              <v-menu
                ref="menu2"
                :close-on-content-click="false"
                v-model="newSemester.autumn.endMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.autumn.endDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.autumn.endDate"
                  label="结束日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.autumn.endDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.autumn.endMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu2.save(newSemester.autumn.endDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <br/>
          <h3>冬季学期</h3>
          <v-layout row wrap>
            <v-flex xs6>
              <v-menu
                ref="menu3"
                :close-on-content-click="false"
                v-model="newSemester.winter.startMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.winter.startDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.winter.startDate"
                  label="开始日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.winter.startDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.winter.startMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu3.save(newSemester.winter.startDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs6>
              <v-menu
                ref="menu4"
                :close-on-content-click="false"
                v-model="newSemester.winter.endMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.winter.endDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.winter.endDate"
                  label="结束日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.winter.endDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.winter.endMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu4.save(newSemester.winter.endDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <br/>
          <h3>春季学期</h3>
          <v-layout row wrap>
            <v-flex xs6>
              <v-menu
                ref="menu5"
                :close-on-content-click="false"
                v-model="newSemester.spring.startMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.spring.startDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.spring.startDate"
                  label="开始日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.spring.startDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.spring.startMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu5.save(newSemester.spring.startDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs6>
              <v-menu
                ref="menu6"
                :close-on-content-click="false"
                v-model="newSemester.spring.endMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.spring.endDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.spring.endDate"
                  label="结束日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.spring.endDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.spring.endMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu6.save(newSemester.spring.endDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <br/>
          <h3>夏季学期</h3>
          <v-layout row wrap>
            <v-flex xs6>
              <v-menu
                ref="menu7"
                :close-on-content-click="false"
                v-model="newSemester.summer.startMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.summer.startDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.summer.startDate"
                  label="开始日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.summer.startDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.summer.startMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu7.save(newSemester.summer.startDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
            <v-flex xs6>
              <v-menu
                ref="menu8"
                :close-on-content-click="false"
                v-model="newSemester.summer.endMenu"
                :nudge-right="40"
                :return-value.sync="newSemester.summer.endDate"
                lazy
                transition="scale-transition"
                offset-y
                full-width
                max-width="290px"
                min-width="290px"
              >
                <v-text-field
                  slot="activator"
                  v-model="newSemester.summer.endDate"
                  label="结束日期"
                  prepend-icon="event"
                  readonly
                ></v-text-field>
                <v-date-picker
                  v-model="newSemester.summer.endDate"
                  no-title
                  scrollable
                >
                  <v-spacer></v-spacer>
                  <v-btn flat color="primary" @click="newSemester.summer.endMenu = false">取消</v-btn>
                  <v-btn flat color="primary" @click="$refs.menu8.save(newSemester.summer.endDate)">确认</v-btn>
                </v-date-picker>
              </v-menu>
            </v-flex>
          </v-layout>
          <v-btn color="primary" @click="addSemester()">确认</v-btn>
        </v-form>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Semester',
  data: () => ({
    tab: null,
    menu: false,
    headers: [
      {
        text: '编号',
        value: 'id'
      },
      {
        text: '学年',
        value: 'year'
      },
      {
        text: '学期',
        value: 'season'
      },
      {
        text: '开始日期',
        value: 'start_date'
      },
      {
        text: '结束日期',
        value: 'end_date'
      },
      {
        text: '是否开通选课',
        value: 'status'
      },
      {
        text: '开通选课',
        value: 'id',
        sortable: false
      }
    ],
    semesters: [
    ],
    newSemester: {
      valid: true,
      year: null,
      autumn: {
        startDate: null,
        endDate: null
      },
      winter: {
        startDate: null,
        endDate: null
      },
      spring: {
        startDate: null,
        endDate: null
      },
      summer: {
        startDate: null,
        endDate: null
      }
    }
  }),
  mounted: function () {
    this.getSemesters()
  },
  methods: {
    getSemesters: function () {
      this.$axios.get('semester/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.semesters.push({
              id: response.data[i].id,
              year: response.data[i].year,
              season: response.data[i].season,
              startDate: response.data[i].start_date,
              endDate: response.data[i].end_date,
              status: response.data[i].status
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    openSemesterCourse: function (semesterId) {
      this.$axios.post('semester/status/', {'semester_id': semesterId, 'operation': 1})
        .then(response => {
          if ('detail' in response.data && response.data['detail'] === 0) {
            for (let i = 0; i < this.semesters.length; i++) {
              this.semesters[i].status = false
            }
            this.semesters[semesterId].status = true
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    closeSemesterCourse: function (semesterId) {
      this.$axios.post('semester/status/', {'semester_id': semesterId, 'operation': 2})
        .then(response => {
          if ('detail' in response.data && response.data['detail'] === 0) {
            this.semesters[semesterId].status = false
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    addSemester: function () {
      if (this.$refs.semesterForm.validate()) {
        let semesterData = JSON.stringify({
          year: this.newSemester.year,
          autumn_start_date: this.newSemester.autumn.startDate,
          autumn_end_date: this.newSemester.autumn.endDate,
          winter_start_date: this.newSemester.winter.startDate,
          winter_end_date: this.newSemester.winter.endDate,
          spring_start_date: this.newSemester.spring.startDate,
          spring_end_date: this.newSemester.spring.endDate,
          summer_start_date: this.newSemester.summer.startDate,
          summer_end_date: this.newSemester.summer.endDate
        })
        this.$axios.post('semester/', semesterData)
          .then(response => {
            if ('detail' in response.data && response.data['detail'] === 0) {
              window.alert('添加成功！')
              this.semesters = []
              this.getSemesters()
            }
          })
          .catch(error => {
            window.alert(error)
          })
      }
    }
  }
}
</script>

<style>
</style>
