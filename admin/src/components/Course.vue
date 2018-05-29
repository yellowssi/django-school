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
        <v-data-table
          :headers="courseHeaders"
          :items="courses"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
            <td>{{ props.item.college_name }}</td>
            <td>{{ props.item.credit }}</td>
            <td>{{ props.item.time }}</td>
            <td>
              <v-btn icon @click="deleteCourse(props.item.id)">
                <v-icon color="error">clear</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        新增课程
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="semesterHeaders"
          :items="semesters"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.year }}</td>
            <td>{{ props.item.season }}</td>
            <td>{{ props.item.start_date }}</td>
            <td>{{ props.item.end_date }}</td>
            <td>
              <v-btn icon @click="getSemesterCourses(props.item.id)">
                <v-icon color="success">event</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
        <br/>
        <v-divider></v-divider>
        <br/>
        <v-data-table
          :headers="semesterCourseHeaders"
          :items="semesterCourses"
          item-key="id"
          v-show="semesterChoosed">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.course_id }}</td>
            <td>{{ props.item.course_name }}</td>
            <td>{{ props.item.teacher_name }}</td>
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.number }}</td>
          </template>
        </v-data-table>
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
    tab: null,
    courses: [],
    courseHeaders: [
      {
        text: '课程编号',
        value: 'id'
      },
      {
        text: '课程名称',
        value: 'name'
      },
      {
        text: '所属学院',
        value: 'college_name'
      },
      {
        text: '学分',
        value: 'credit'
      },
      {
        text: '学时',
        value: 'time'
      }
    ],
    semesterChoosed: null,
    semesterCourses: [],
    semesterCourseHeaders: [
      {
        text: '课程编号',
        value: 'course_id'
      },
      {
        text: '课程名称',
        value: 'course_name'
      },
      {
        text: '教师',
        value: 'teacher_name'
      },
      {
        text: '上课时间',
        value: 'time'
      },
      {
        text: '容量',
        value: 'number'
      }
    ],
    teachers: [],
    semesters: [
    ],
    semesterHeaders: [
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
        text: '该学期课程',
        value: 'id',
        sortable: false
      }
    ],
    colleges: [],
    newCourse: {},
    newSemesterCourse: {}
  }),
  mounted: function () {
    this.getColleges()
    this.getCourses()
    this.getTeachers()
    this.getSemesters()
  },
  methods: {
    getColleges: function () {
      this.$axios.get('college/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.colleges.push({
              text: response.data[i].name,
              value: response.data[i].id
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getTeachers: function () {
      this.$axios.get('teacher/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.teachers.push({
              text: response.data[i].name,
              value: response.data[i].id
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
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
    getCourses: function () {
      this.$axios.get('course/')
        .then(response => {
          for (let i = 0; i < response.data.length; i++) {
            this.courses.push({
              id: this.response.data[i].id,
              name: this.response.data[i].name,
              college_name: this.response.data[i].college_name,
              credit: this.response.data[i].credit,
              time: this.response.data[i].time
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    deleteCourse: function (courseId) {},
    getSemesterCourses: function (semesterId) {
      this.semesterChoosed = semesterId
    },
    addCourse: function () {},
    addSemesterCourse: function () {},
    deleteSemesterCourse: function (semesterCourseId) {}
  }
}
</script>
