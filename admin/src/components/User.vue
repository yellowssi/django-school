<template>
  <div class="User">
    <v-toolbar color="cyan" dark tabs>
      <v-toolbar-title>用户管理</v-toolbar-title>
      <v-tabs
        slot="extension"
        v-model="tab"
        centered
        color="cyan"
        slider-color="yellow"
      >
        <v-tab>
          管理员
        </v-tab>
        <v-tab>
          教师
        </v-tab>
        <v-tab>
          学生
        </v-tab>
        <v-tab>
          学院
        </v-tab>
        <v-tab>
          新建用户
        </v-tab>
      </v-tabs>
    </v-toolbar>
    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-data-table
          :headers="adminHeaders"
          :items="admins"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
            <td>{{ (props.item.gender === 'male') ? '男' : '女' }}</td>
            <td>{{ props.item.birth }}</td>
            <td>{{ props.item.mobile }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="teacherHeaders"
          :items="teachers"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
            <td>{{ (props.item.gender === 'male') ? '男' : '女' }}</td>
            <td>{{ props.item.birth }}</td>
            <td>{{ props.item.mobile }}</td>
            <td>{{ props.item.title }}</td>
            <td>{{ props.item.salary }}</td>
            <td>{{ props.item.college_name }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="studentHeaders"
          :items="students"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
            <td>{{ (props.item.gender === 'male') ? '男' : '女' }}</td>
            <td>{{ props.item.birth }}</td>
            <td>{{ props.item.mobile }}</td>
            <td>{{ props.item.origin }}</td>
            <td>{{ props.item.college_name }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-data-table
          :headers="collegeHeaders"
          :items="colleges"
          item-key="id">
          <template slot="items" slot-scope="props">
            <td>{{ props.item.id }}</td>
            <td>{{ props.item.name }}</td>
            <td>{{ props.item.address }}</td>
            <td>{{ props.item.tel }}</td>
          </template>
        </v-data-table>
      </v-tab-item>
      <v-tab-item>
        <v-form ref="addUserForm" v-model="newUser.valid" lazy-validation>
          <v-text-field
            label="编号"
            v-model="newUser.id"
            :rules="newUser.idRules"
            hint="编号为8位"
            required></v-text-field>
          <v-text-field
            label="姓名"
            v-model="newUser.name"
            :rules="newUser.nameRules"
            required></v-text-field>
          <v-select
            label="性别"
            :items="[{text: '男', value: 'male'}, {text: '女', value: 'female'}]"
            v-model="newUser.gender"></v-select>
          <v-menu
            ref="menu"
            :close-on-content-click="false"
            v-model="menu"
            :nudge-right="40"
            :return-value.sync="newUser.birth"
            lazy
            transition="scale-transition"
            offset-y
            full-width
            max-width="290px"
            min-width="290px"
          >
            <v-text-field
              slot="activator"
              v-model="newUser.birth"
              label="生日"
              prepend-icon="event"
              readonly
            ></v-text-field>
            <v-date-picker
              v-model="newUser.birth"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn flat color="primary" @click="menu = false">取消</v-btn>
              <v-btn flat color="primary" @click="$refs.menu.save(newUser.birth)">确认</v-btn>
            </v-date-picker>
          </v-menu>
          <v-text-field
            label="电话"
            v-model="newUser.mobile"
            :rules="newUser.mobileRules"
            required></v-text-field>
        </v-form>
        <v-select
          label="身份"
          :items="[{text:'学生',value:1},{text:'教师',value:2},{text:'管理员',value:3}]"
          v-model="newUser.identity"
          required></v-select>
        <v-text-field
          label="籍贯"
          v-if="newUser.identity === 1"
          v-model="newUser.origin"
          required></v-text-field>
        <v-select
          label="职称"
          v-if="newUser.identity === 2"
          :items="[{text:'教授',value:'professor'},{text:'副教授',value:'associate'},{text:'讲师',value:'lecturer'},{text:'助教',value:'assistant'}]"
          v-model="newUser.title"
          required></v-select>
        <v-text-field
          label="薪水"
          v-if="newUser.identity === 2"
          v-model="newUser.salary"
          required></v-text-field>
        <v-select
          label="学院"
          v-if="newUser.identity === 1 || newUser.identity === 2"
          :items="collegeChoices"
          v-model="newUser.college_id"
          required></v-select>
        <v-text-field
          label="密码"
          v-model="newUser.password"
          type="password"></v-text-field>
        <v-btn color="primary" @click="addUser()">确认</v-btn>
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  name: 'User',
  data: () => ({
    tab: null,
    menu: false,
    admins: [],
    adminHeaders: [
      {
        text: '工号',
        value: 'id'
      },
      {
        text: '姓名',
        value: 'name'
      },
      {
        text: '性别',
        value: 'gender'
      },
      {
        text: '出生日期',
        value: 'birth'
      },
      {
        text: '电话',
        value: 'mobile'
      }
    ],
    teachers: [],
    teacherHeaders: [
      {
        text: '工号',
        value: 'id'
      },
      {
        text: '姓名',
        value: 'name'
      },
      {
        text: '性别',
        value: 'gender'
      },
      {
        text: '出生日期',
        value: 'birth'
      },
      {
        text: '电话',
        value: 'mobile'
      },
      {
        text: '职称',
        value: 'title'
      },
      {
        text: '薪水',
        value: 'salary'
      },
      {
        text: '学院',
        value: 'college_name'
      }
    ],
    students: [],
    studentHeaders: [
      {
        text: '学号',
        value: 'id'
      },
      {
        text: '姓名',
        value: 'name'
      },
      {
        text: '性别',
        value: 'gender'
      },
      {
        text: '出生日期',
        value: 'birth'
      },
      {
        text: '电话',
        value: 'mobile'
      },
      {
        text: '籍贯',
        value: 'origin'
      },
      {
        text: '学院',
        value: 'college_name'
      }
    ],
    colleges: [],
    collegeHeaders: [
      {
        text: '编号',
        value: 'id'
      },
      {
        text: '名称',
        value: 'name'
      },
      {
        text: '地址',
        value: 'address'
      },
      {
        text: '电话',
        value: 'tel'
      }
    ],
    collegeChoices: [],
    newUser: {
      valid: true,
      identity: null,
      id: null,
      name: null,
      gender: null,
      birth: null,
      mobile: null,
      origin: null,
      title: null,
      salary: null,
      college_id: null,
      password: null
    }
  }),
  mounted: function () {
    this.getColleges()
    this.getStudents()
    this.getTeachers()
    this.getAdmins()
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
            this.colleges.push({
              id: response.data['colleges'][i].id,
              name: response.data['colleges'][i].name,
              address: response.data['colleges'][i].address,
              tel: response.data['colleges'][i].tel
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getStudents: function () {
      this.$axios.get('student/')
        .then(response => {
          for (let i = 0; i < response.data['students'].length; i++) {
            this.students.push({
              id: response.data['students'][i].id,
              name: response.data['students'][i].name,
              gender: response.data['students'][i].gender,
              birth: response.data['students'][i].birth,
              mobile: response.data['students'][i].mobile,
              origin: response.data['students'][i].origin,
              college_name: response.data['students'][i].college_name
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
            this.students.push({
              id: response.data['teachers'][i].id,
              name: response.data['teachers'][i].name,
              gender: response.data['teachers'][i].gender,
              birth: response.data['teachers'][i].birth,
              mobile: response.data['teachers'][i].mobile,
              title: response.data['teachers'][i].title,
              salary: response.data['teachers'][i].salary,
              college_name: response.data['teachers'][i].college_name
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    getAdmins: function () {
      this.$axios.get('admin/')
        .then(response => {
          for (let i = 0; i < response.data['admins'].length; i++) {
            this.students.push({
              id: response.data['admins'][i].id,
              name: response.data['admins'][i].name,
              gender: response.data['admins'][i].gender,
              birth: response.data['admins'][i].birth,
              mobile: response.data['admins'][i].mobile
            })
          }
        })
        .catch(error => {
          window.alert(error)
        })
    },
    addUser: function () {
      if (this.newUser.identity === 1) {
        let newUserData = JSON.stringify({
          id: this.newUser.id,
          name: this.newUser.name,
          gender: this.newUser.gender,
          birth: this.newUser.birth,
          mobile: this.newUser.mobile,
          origin: this.newUser.origin,
          college_id: this.newUser.college_id,
          password: this.newUser.password
        })
        this.$axios.post('register/', newUserData)
          .then(response => {
            if ('detail' in response.data && response.data['detail'] === 0) {
              window.alert('创建成功')
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
