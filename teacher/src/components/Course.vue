<template>
  <div class="Course">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>授课课程</v-toolbar-title>
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
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.number }}</td>
            <td>
              <v-btn icon @click="getStudentsList(props.item.id)">
                <v-icon color="success">list</v-icon>
              </v-btn>
            </td>
          </template>
        </v-data-table>
        <v-data-table
          :headers="studentHeaders"
          :items="students"
          item-key="id"
          v-show="students">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.studentId }}</td>
            <td>{{ props.item.studentName }}</td>
            <td>{{ (props.item.studentGender === 'male') ? '男' : '女' }}</td>
            <td>{{ props.item.studentCollege }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="nextSemesterCourseHeaders"
          :items="nextSemesterCourses"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.courseCredit }}</td>
            <td>{{ props.item.time }}</td>
            <td>{{ props.item.number }}</td>
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
        text: '上课时间',
        value: 'time'
      },
      {
        text: '人数/容量',
        value: 'number'
      },
      {
        text: '学生名单',
        value: 'id',
        sortable: false
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
        text: '上课时间',
        value: 'time'
      },
      {
        text: '人数/容量',
        value: 'number'
      }
    ],
    students: [],
    studentHeaders: [
      {
        text: '学号',
        value: 'studentId'
      },
      {
        text: '姓名',
        value: 'studentName'
      },
      {
        text: '性别',
        value: 'studentGender'
      },
      {
        text: '学院',
        value: 'studentCollege'
      }
    ]
  }),
  mounted: function () {
    this.getSemesterCourses()
    this.getNextSemesterCourses()
  },
  methods: {
    getSemesterCourses: function () {
      this.$axios.get('course/')
        .then(response => {
          for (let i = 0; i < response.data['courses'].length; i++) {
            this.semesterCourses.push({
              id: response.data['courses'][i].id,
              courseId: response.data['courses'][i].course_id,
              courseName: response.data['courses'][i].course_name,
              courseCredit: response.data['courses'][i].course_credit,
              time: response.data['courses'][i].time,
              number: response.data['courses'][i].number
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getNextSemesterCourses: function () {
      this.$axios.get('course/next/')
        .then(response => {
          for (let i = 0; i < response.data['courses'].length; i++) {
            this.nextSemesterCourses.push({
              id: response.data['courses'][i].id,
              courseId: response.data['courses'][i].course_id,
              courseName: response.data['courses'][i].course_name,
              courseCredit: response.data['courses'][i].course_credit,
              time: response.data['courses'][i].time,
              number: response.data['courses'][i].number
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getStudentsList: function (courseId) {
      this.$axios.get('course/students-list/' + courseId + '/')
        .then(response => {
          this.students = []
          for (let i = 0; i < response.data['students'].length; i++) {
            this.students.push({
              id: response.data['students'][i].id,
              studentId: response.data['students'][i].student_id,
              studentName: response.data['students'][i].student_name,
              studentGender: response.data['students'][i].student_gender,
              studentCollege: response.data['students'][i].student_college
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    }
  }
}
</script>
