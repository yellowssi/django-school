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
            <td>{{ props.item.collegeName }}</td>
            <td>{{ props.item.credit }}</td>
            <td>{{ props.item.time }}</td>
            <td>
              <v-btn icon @click="delCourse(props.item.id)">
                <v-icon color="error">clear</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-form ref="addCourseForm" v-model="newCourse.valid" lazy-validation>
          <v-text-field
            label="课程编号"
            v-model="newCourse.id"
            :rules="newCourse.idRules"
            required></v-text-field>
          <v-text-field
            label="课程名称"
            v-model="newCourse.name"
            :rules="newCourse.nameRules"
            required></v-text-field>
          <v-select
            label="学院"
            :items="collegeChoices"
            v-model="newCourse.collegeId"
            required></v-select>
          <v-text-field
            label="学分"
            v-model="newCourse.credit"
            :rules="newCourse.creditRules"
            required></v-text-field>
          <v-text-field
            label="学时"
            v-model="newCourse.time"
            :rules="newCourse.timeRules"
            required></v-text-field>
          <v-btn color="primary" @click="addCourse()">添加</v-btn>
        </v-form>
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="semesterHeaders"
          :items="semesters"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.year }}</td>
            <td>{{ (props.item.season === 'autumn') ? '秋季学期' : ((props.item.season === 'winter') ? '冬季学期' : (props.item.season === 'spring') ? '春季学期' : '夏季学期') }}</td>
            <td>{{ props.item.startDate }}</td>
            <td>{{ props.item.endDate }}</td>
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
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.teacherName }}</td>
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.number }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-form ref="addSemesterCourseForm" v-model="newSemesterCourse.valid" lazy-validation>
          <v-select
            :items="courseChoices"
            label="课程"
            v-model="newSemesterCourse.courseId"
            required></v-select>
          <v-select
            :items="semesterChoices"
            label="学期"
            v-model="newSemesterCourse.semesterId"
            required></v-select>
          <v-select
            :items="teacherChoices"
            label="教师"
            v-model="newSemesterCourse.teacherId"
            required></v-select>
          <v-text-field
            label="上课时间"
            v-model="newSemesterCourse.time"
            required></v-text-field>
          <v-text-field
            label="容量"
            v-model="newSemesterCourse.number"
            required></v-text-field>
          <v-btn color="primary" @click="addSemesterCourse()">添加</v-btn>
        </v-form>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Course',
  data: () => ({
    tab: null,
    courseChoices: [],
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
        value: 'collegeName'
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
        text: '上课时间',
        value: 'time'
      },
      {
        text: '容量',
        value: 'number'
      }
    ],
    teacherChoices: [],
    semesterChoices: [],
    semesters: [],
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
        value: 'startDate'
      },
      {
        text: '结束日期',
        value: 'endDate'
      },
      {
        text: '该学期课程',
        value: 'id',
        sortable: false
      }
    ],
    collegeChoices: [],
    newCourse: {
      valid: true,
      id: null,
      name: null,
      collegeId: null,
      credit: null,
      time: null
    },
    newSemesterCourse: {
      valid: true,
      courseId: null,
      semesterId: null,
      teacherId: null,
      time: null,
      number: null
    }
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
          for (let i = 0; i < response.data['colleges'].length; i++) {
            this.collegeChoices.push({
              text: response.data['colleges'][i].name,
              value: response.data['colleges'][i].id
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
          for (let i = 0; i < response.data['teachers'].length; i++) {
            this.teacherChoices.push({
              text: response.data['teachers'][i].id + '/' + response.data['teachers'][i].name,
              value: response.data['teachers'][i].id
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
          for (let i = 0; i < response.data['semesters'].length; i++) {
            this.semesters.push({
              id: response.data['semesters'][i].id,
              year: response.data['semesters'][i].year,
              season: response.data['semesters'][i].season,
              startDate: response.data['semesters'][i].start_date,
              endDate: response.data['semesters'][i].end_date,
              status: response.data['semesters'][i].status
            })
            this.semesterChoices.push({
              text: response.data['semesters'][i].year + ((response.data['semesters'][i].season === 'autumn') ? '秋季学期' : ((response.data['semesters'][i].season === 'winter') ? '冬季学期' : (response.data['semesters'][i].season === 'spring') ? '春季学期' : '夏季学期')),
              value: response.data['semesters'][i].id
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
          for (let i = 0; i < response.data['courses'].length; i++) {
            this.courses.push({
              id: response.data['courses'][i].id,
              name: response.data['courses'][i].name,
              collegeName: response.data['courses'][i].college_name,
              credit: response.data['courses'][i].credit,
              time: response.data['courses'][i].time
            })
            this.courseChoices.push({
              text: response.data['courses'][i].college_name + '/' + response.data['courses'][i].name,
              value: response.data['courses'][i].id
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    delCourse: function (courseId) {
      this.$axios.post('course/', {'operation': 2, 'course_id': courseId})
        .then(response => {
          if ('detail' in response.data && response.data['detail'] === 0) {
            window.alert('删除成功!')
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getSemesterCourses: function (semesterId) {
      this.semesterChoosed = semesterId
      this.$axios.get('semester-course/' + semesterId + '/')
        .then(response => {
          this.semesterCourses = []
          for (let i = 0; i < response.data['semester_courses'].length; i++) {
            this.semesterCourses.push({
              id: response.data['semester_courses'][i].id,
              courseId: response.data['semester_courses'][i].course_id,
              courseName: response.data['semester_courses'][i].course_name,
              teacherName: response.data['semester_courses'][i].teacher_name,
              credit: response.data['semester_courses'][i].credit,
              time: response.data['semester_courses'][i].time,
              number: response.data['semester_courses'][i].number
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    addCourse: function () {
      if (this.$refs.addCourseForm.validate()) {
        let courseData = JSON.stringify({
          operation: 1,
          id: this.newCourse.id,
          name: this.newCourse.name,
          college_id: this.newCourse.collegeId,
          credit: this.newCourse.credit,
          time: this.newCourse.time
        })
        this.$axios.post('course/', courseData)
          .then(response => {
            if ('detail' in response.data && response.data['detail'] === 0) {
              window.alert('添加成功!')
            }
          })
          .catch(error => {
            window.alert(error)
          })
      }
    },
    addSemesterCourse: function () {
      if (this.$refs.addSemesterCourseForm.validate()) {
        let semesterCourseData = JSON.stringify({
          operation: 1,
          semester_id: this.newSemesterCourse.semesterId,
          course_id: this.newSemesterCourse.courseId,
          teacher_id: this.newSemesterCourse.teacherId,
          time: this.newSemesterCourse.time,
          number: this.newSemesterCourse.number
        })
        this.$axios.post('semester-course/', semesterCourseData)
          .then(response => {
            if ('detail' in response.data && response.data['detail'] === 0) {
              window.alert('添加成功!')
            }
          })
          .catch(error => {
            window.alert(error)
          })
      }
    },
    delSemesterCourse: function (semesterCourseId) {
      this.$axios.post('semester-course/', {'operation': 2, 'semester_course_id': semesterCourseId})
        .then(response => {
          if ('detail' in response.data && response.data['detail'] === 0) {
            window.alert('删除成功!')
          }
        })
        .catch(error => {
          window.alert(error)
        })
    }
  }
}
</script>
