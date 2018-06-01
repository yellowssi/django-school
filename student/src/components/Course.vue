<template>
  <div class="Course">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>选课系统</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="tab"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab>
          本学期课表
        </v-tab>
        <v-tab>
          选课
        </v-tab>
        <v-tab>
          下学期课表
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-data-table
          :headers="semesterCourseHeaders"
          :items="semesterCourses"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.courseCredit }}</td>
            <td>{{ props.item.teacherName }}</td>
            <td>{{ props.item.time }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <h3 v-show="!searchCourseInfo.status">选课时间未到!</h3>
        <h3 v-show="searchCourseInfo.status">{{ searchCourseInfo.semester }}</h3>
        <v-text-field
          label="课程编号"
          v-model="searchCourseInfo.courseId"
          v-show="searchCourseInfo.status"></v-text-field>
        <v-text-field
          label="课程名称"
          v-model="searchCourseInfo.courseName"
          v-show="searchCourseInfo.status"></v-text-field>
        <v-btn color="primary" @click="searchCourse()" v-show="searchCourseInfo.status">搜索</v-btn>
        <v-data-table
          :headers="courseHeaders"
          :items="courses"
          item-key="id"
          v-show="searchCourseInfo.searched">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.teacherName }}</td>
            <td>{{ props.item.credit }}</td>
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.number }}</td>
            <td>
              <v-btn icon @click="addCourse(props.item.id)">
                <v-icon color="success">done</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <h3 v-show="!searchCourseInfo.status">选课时间未到!</h3>
        <v-data-table
          :headers="nextSemesterCourseHeaders"
          :items="nextSemesterCourses"
          item-key="id"
          v-show="searchCourseInfo.status">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.courseCredit }}</td>
            <td>{{ props.item.teacherName }}</td>
            <td>{{ props.item.time }}</td>
            <td>
              <v-btn icon @click="delCourse(props.item.id)">
                <v-icon color="error">clear</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
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
        value: 'courseId'
      },
      {
        text: '课程名称',
        value: 'courseName'
      },
      {
        text: '教师',
        value: 'teacherName'
      },
      {
        text: '学分',
        value: 'credit'
      },
      {
        text: '上课时间',
        value: 'time'
      },
      {
        text: '课程容量',
        value: 'number'
      },
      {
        text: '选课',
        value: 'id',
        sortable: false
      }
    ],
    semesterCourses: [],
    nextSemesterCourses: [],
    semesterCourseHeaders: [
      {
        text: '课程编号',
        value: 'courseId'
      },
      {
        text: '课程名称',
        value: 'courseName'
      },
      {
        text: '学分',
        value: 'courseCredit'
      },
      {
        text: '教师',
        value: 'teacherName'
      },
      {
        text: '上课时间',
        value: 'time'
      }
    ],
    nextSemesterCourseHeaders: [
      {
        text: '课程编号',
        value: 'courseId'
      },
      {
        text: '课程名称',
        value: 'courseName'
      },
      {
        text: '学分',
        value: 'courseCredit'
      },
      {
        text: '教师',
        value: 'teacherName'
      },
      {
        text: '上课时间',
        value: 'time'
      },
      {
        text: '退课',
        value: 'id',
        sortable: false
      }
    ],
    searchCourseInfo: {
      status: false,
      semester: null,
      searched: false,
      courseId: null,
      courseName: null
    }
  }),
  mounted: function () {
    this.checkSemesterStatus()
    this.getSemesterCourse()
  },
  methods: {
    checkSemesterStatus: function () {
      this.$axios.get('semester/')
        .then(response => {
          if ('semester_info' in response.data) {
            this.searchCourseInfo.status = true
            this.searchCourseInfo.semseter = response.data['semester_info']
            this.getNextSemesterCourse()
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getSemesterCourse: function () {
      this.$axios.get('course/')
        .then(response => {
          for (let i = 0; i < response.data['courses'].length; i++) {
            this.semesterCourses.push({
              id: response.data['courses'][i].id,
              courseId: response.data['courses'][i].course_id,
              courseName: response.data['courses'][i].course_name,
              courseCredit: response.data['courses'][i].course_credit,
              teacherName: response.data['courses'][i].teacher_name,
              time: response.data['courses'][i].time
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getNextSemesterCourse: function () {
      this.$axios.get('course/next/')
        .then(response => {
          for (let i = 0; i < response.data['courses'].length; i++) {
            this.nextSemesterCourses.push({
              id: response.data['courses'][i].id,
              courseId: response.data['courses'][i].course_id,
              courseName: response.data['courses'][i].course_name,
              courseCredit: response.data['courses'][i].course_credit,
              teacherName: response.data['courses'][i].teacher_name,
              time: response.data['courses'][i].time
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    searchCourse: function () {
      let Info = JSON.stringify({
        course_id: this.searchCourseInfo.courseId,
        course_name: this.searchCourseInfo.courseName
      })
      this.$axios.post('course/next/search/', Info)
        .then(response => {
          this.searchCourseInfo.searched = true
          this.courses = []
          for (let i = 0; i < response.data['semester_courses'].length; i++) {
            this.courses.push({
              id: response.data['semester_courses'][i].id,
              courseId: response.data['semester_courses'][i].course_id,
              courseName: response.data['semester_courses'][i].course_name,
              credit: response.data['semester_courses'][i].credit,
              teacherName: response.data['semester_courses'][i].teacher_name,
              time: response.data['semester_courses'][i].time,
              number: response.data['semester_courses'][i].number
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    addCourse: function (courseId) {
      let Info = JSON.stringify({
        operation: 1,
        semester_course_id: courseId
      })
      this.$axios.post('course/next/', Info)
        .then(response => {
          if ('detail' in response.data) {
            window.alert(response.data['detail'])
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    delCourse: function (courseId) {
      let Info = JSON.stringify({
        operation: 2,
        semester_course_id: courseId
      })
      this.$axios.post('course/next/', Info)
        .then(response => {
          if ('detail' in response.data) {
            window.alert(response.data['detail'])
          }
        })
        .catch(error => {
          window.alert(error)
        })
    }
  }
}
</script>
