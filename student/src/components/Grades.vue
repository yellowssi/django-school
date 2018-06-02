<template>
  <div class="Grades">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>成绩查询</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="tab"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab>
          本学期成绩
        </v-tab>
        <v-tab>
          成绩大表
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-data-table
          :headers="gradesHeaders"
          :items="semesterGrades"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.courseCredit }}</td>
            <td>{{ props.item.sgrade }}</td>
            <td>{{ props.item.gpa }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="gradesHeaders"
          :items="allGrades"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.courseId }}</td>
            <td>{{ props.item.courseName }}</td>
            <td>{{ props.item.courseCredit }}</td>
            <td>{{ props.item.sgrade }}</td>
            <td>{{ props.item.gpa }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'Grades',
  data: () => ({
    tab: null,
    semesterGPA: null,
    semesterGrades: [],
    allGPA: null,
    allGrades: [],
    gradesHeaders: [
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
        text: '总成绩',
        value: 'sgrade'
      },
      {
        text: '绩点',
        value: 'gpa'
      }
    ]
  }),
  mounted: function () {
    this.getSemesterGrades()
    this.getAllGrades()
  },
  methods: {
    getCourseGPA: function (grades) {
      if (grades >= 90 && grades <= 100) {
        return 4.0
      } else if (grades >= 85 && grades <= 89.9) {
        return 3.7
      } else if (grades >= 82 && grades <= 84.9) {
        return 3.3
      } else if (grades >= 78 && grades <= 81.9) {
        return 3.0
      } else if (grades >= 75 && grades <= 77.9) {
        return 2.7
      } else if (grades >= 72 && grades <= 74.9) {
        return 2.3
      } else if (grades >= 68 && grades <= 71.9) {
        return 2.0
      } else if (grades >= 66 && grades <= 67.9) {
        return 1.7
      } else if (grades >= 64 && grades <= 65.9) {
        return 1.5
      } else if (grades >= 60 && grades <= 63.9) {
        return 1.0
      } else {
        return 0.0
      }
    },
    getAverageGPA: function () {
      let credits = 0
      let gpa = 0.0
      for (let i = 0; i < this.semesterGrades.length; i++) {
        credits += this.semesterGrades[i].courseCredit
        gpa += this.semesterGrades[i].gpa * this.semesterGrades[i].courseCredit
      }
      this.semesterGPA = gpa / credits
      credits = 0
      gpa = 0.0
      for (let i = 0; i < this.allGrades.length; i++) {
        credits += this.allGrades[i].courseCredit
        gpa += this.allGrades[i].gpa * this.allGrades[i].courseCredit
      }
      this.allGPA = gpa / credits
    },
    getSemesterGrades: function () {
      this.$axios.get('grades/semester/')
        .then(response => {
          for (let i = 0; i < response.data['grades'].length; i++) {
            this.semesterGrades.push({
              courseId: response.data['grades'][i].course_id,
              courseName: response.data['grades'][i].course_name,
              courseCredit: response.data['grades'][i].course_credit,
              sgrade: response.data['grades'][i].sgrade,
              gpa: this.getCourseGPA(response.data['grades'][i].sgrade)
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getAllGrades: function () {
      this.$axios.get('grades/all/')
        .then(response => {
          for (let i = 0; i < response.data['grades'].length; i++) {
            this.allGrades.push({
              courseId: response.data['grades'][i].course_id,
              courseName: response.data['grades'][i].course_name,
              courseCredit: response.data['grades'][i].course_credit,
              sgrade: response.data['grades'][i].sgrade,
              gpa: this.getCourseGPA(response.data['grades'][i].sgrade)
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

<style>
</style>
