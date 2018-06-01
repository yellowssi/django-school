<template>
  <div class="Course">
    <v-toolbar>
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
          :headers="courseHeaders"
          :items="semesterCourses"
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
      <v-tab-item>
        <v-data-table
          :headers="courseHeaders"
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
        text: '容量',
        value: 'number'
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
    }
  }
}
</script>
