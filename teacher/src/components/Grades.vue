<template>
  <div class="Grades">
    <v-data-table
      :headers="courseHeaders"
      :items="courses"
      item-key="id">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.courseId }}</td>
        <td>{{ props.item.courseName }}</td>
        <td>{{ props.item.courseCredit }}</td>
        <td>{{ props.item.time }}</td>
        <td>{{ props.item.number }}</td>
        <td>
          <v-btn icon @click="getStudentList(props.item.id)">
            <v-icon color="success">done</v-icon>
          </v-btn>
        </td>
      </template>
    </v-data-table>
    <v-data-table
      :headers="studentHeaders"
      :items="students"
      item-key="id">
      <template slot="items" slot-scope="props">
        <td>{{ props.item.studentId }}</td>
        <td>{{ props.item.studentName }}</td>
        <td>{{ (props.item.studentGender === 'male') ? '男' : '女' }}</td>
        <td>{{ props.item.studentCollege }}</td>
        <td>
          <v-text-field
            v-model="props.item.pgrade"></v-text-field>
        </td>
        <td>
          <v-text-field
            v-model="props.item.egrade"></v-text-field>
        </td>
      </template>
    </v-data-table>
    <v-btn color="primary" @click="sendGrades()">录入</v-btn>
  </div>
</template>

<script>
export default {
  name: 'Grades',
  data: () => ({
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
        text: '学分',
        value: 'courseCredit'
      },
      {
        text: '上课时间',
        value: 'time'
      },
      {
        text: '选课人数/容量',
        value: 'number'
      },
      {
        text: '录入',
        value: 'id',
        sortable: false
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
      },
      {
        text: '平时成绩',
        value: 'pgrade',
        sortable: false
      },
      {
        text: '考试成绩',
        value: 'egrade',
        sortable: false
      }
    ]
  }),
  mounted: function () {
    this.getSemesterCourses()
  },
  methods: {
    getSemesterCourses: function () {
      this.$axios.get('course/')
        .then(response => {
          for (let i = 0; i < response.data['courses'].length; i++) {
            this.courses.push({
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
    getStudentList: function (courseId) {
      this.$axios.get('course/grades/' + courseId + '/')
        .then(response => {
          this.students = []
          for (let i = 0; i < response.data['students'].length; i++) {
            this.students.push({
              id: response.data['students'][i].id,
              studentId: response.data['students'][i].student_id,
              studentName: response.data['students'][i].student_name,
              studentGender: response.data['students'][i].student_gender,
              studentCollege: response.data['students'][i].student_college,
              pgrade: response.data['students'][i].pgrade,
              egrade: response.data['students'][i].egrade
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    sendGrades: function () {
      let grades = JSON.stringify({
        grades: this.students
      })
      this.$axios.post('course/grades/1/', grades)
        .then(response => {
          window.alert('录入成功')
        })
        .catch(error => {
          window.alert(error)
        })
    }
  }
}
</script>

<style>
</style>
