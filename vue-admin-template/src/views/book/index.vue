  <template>
    <div class="app-container">
      <el-row display="margin-top:10px">
        <el-input v-model="input_bookname" placeholder="请输入添加人名" style="display:inline-table; width: 20%; float:left"></el-input>
        <el-input v-model="input_phone" placeholder="请输入金额" style="display:inline-table; width: 20%; float:left"></el-input>
        <el-input v-model="input_relation" placeholder="请输入地址" style="display:inline-table; width: 20%; float:left"></el-input>
        <el-input v-model="input_address" placeholder="请输入关系" style="display:inline-table; width: 20%; float:left"></el-input>
        <el-input v-model="input_money" placeholder="请输入电话" style="display:inline-table; width: 20%; float:left"></el-input>
        <el-button type="primary" @click="addUser()" style="float:left; margin: 2px;">新增</el-button>
      </el-row>
<!--  <el-row display="margin-top:10px">
        <el-input v-model="output_bookname" placeholder="请输入删除人名" style="display:inline-table; width: 30%; float:left"></el-input>
        <el-button type="primary" @click="deleteBook()" style="float:left; margin: 2px;">删除</el-button>
      </el-row>
-->
      <el-row>
        <el-table :data="list_book" element-loading-text="Loading" border fit highlight-current-row>
          <el-table-column align="center" label="序号" width="95">
           <template slot-scope="scope">
             {{ scope.row.pk }}
           </template>
         </el-table-column>
         <el-table-column prop="book_name" align="center" label="姓名">
           <template slot-scope="scope">
             {{ scope.row.fields.book_name }}
           </template>
         </el-table-column>
         <el-table-column prop="money" align="center" label="份子喜钱">
           <template slot-scope="scope">
             {{ scope.row.fields.money }}
           </template>
         </el-table-column>
         <el-table-column prop="address" align="center" label="地址">
           <template slot-scope="scope">
             {{ scope.row.fields.address }}
           </template>
         </el-table-column>
        <el-table-column prop="relation" align="center" label="关系">
           <template slot-scope="scope">
             {{ scope.row.fields.relation }}
           </template>
         </el-table-column>
         <el-table-column prop="phone" align="center" label="电话">
           <template slot-scope="scope">
             {{ scope.row.fields.phone }}
           </template>
         </el-table-column>
         <el-table-column align="center" label="时间">
           <template slot-scope="scope">
             <span>{{ scope.row.fields.add_time }}</span>
           </template>
         </el-table-column>
         <el-table-column align="center" width='190px' label="操作">
           <template slot-scope="scope">
            <el-button type="primary" @click="deleteBook(scope.row.fields.book_name)"  style="float:left; margin: 5px;">删除</el-button>
            <el-button type="primary" @click.native.prevent="editRow(scope.row)"  style="float:right; margin: 5px;">修改</el-button>
           </template>
         </el-table-column>
       </el-table>
     </el-row>
    <!-- 弹窗组件开始-->
    <dialog-component
      v-if="showDialog"
      ref="dialogComponent"
      :dialog-title="dialogTitle"
      :item-info="tableItem"
      @closeDialog="closeDialog"
    ></dialog-component>
    <!-- 弹窗组件结束-->
   </div>
 </template>

 <script>
   import {
     getList,
     addbook,
     deletebook,
     update_book
   } from '@/api/book'

   import DialogComponent from "./dialogComponent";

   export default {

     name: "DialogDemo",
     components: { DialogComponent },

     filters: {
       statusFilter(status) {
         const statusMap = {
           published: 'success',
           draft: 'gray',
           deleted: 'danger'
         }
         return statusMap[status]
       }
     },
     data() {
       return {

         tableLoading: false,
         showDialog: false,
         dialogTitle: "添加客人",
         tableData: [],
         tableItem: {
            id: "",
            book_name: "",
            money: "",
            address: "",
            relation: "",
            phone: "",
          },

         list_book: null,
         listLoading: true,
         input_bookname: '',
         input_phone: '',
         input_relation: '',
         input_address: '',
         input_money: '',
         output_bookname: ''
       }
     },

    mounted() {
     this.fetchData();
     },

     created() {
       this.getList()
     },
     methods: {
      fetchData() {
        const that = this;
        that.tableLoading = true;
        that.tableData = [
        {
             book_name : 'wxm',
             money : '100',
             phone : '17551017364',
             relation : 'pengyou',
             address : 'qianshan'
        },
        {
             book_name : 'wam',
             money : '100',
             phone : '17551017364',
             relation : 'pengyou',
             address : 'qianshan'
        },

        {
             book_name : 'wbm',
             money : '100',
             phone : '17551017364',
             relation : 'pengyou',
             address : 'qianshan'
        },
        {
             book_name : 'wcm',
             money : '100',
             phone : '17551017364',
             relation : 'pengyou',
             address : 'qianshan'
        }
        ]
      setTimeout(() => {
        that.tableLoading = false;
      }, 1500);
    },
    // 添加操作
    addItem() {
      this.tableItem = {
        id: "",
        book_name: "",
        money: "",
        address: "",
        relation: "",
        phone: "",
      };
      this.dialogTitle = "添加人员";
      this.showDialog = true;
      this.$nextTick(() => {
        this.$refs["dialogComponent"].showDialog = true;
      });
    },
    // 编辑操作
    editRow(row) {
      this.tableItem = row;
      this.dialogTitle = "编辑人员";
      this.showDialog = true;
      // this.update_book(this.tableItem)
      this.$nextTick(() => {
        this.$refs["dialogComponent"].showDialog = true;
      });
    },
    // 关闭操作
    closeDialog(flag) {
      if (flag) {
        // 重新刷新表格内容
        this.fetchData();
      }
      this.showDialog = false;
    },
       getList() {
         this.listLoading = true
         getList().then(response => {
           if (response.error_num === 0) {
             this.list_book = response['list']
             this.listLoading = false
           } else {
             this.$message.error('查询客人信息失败')
             console.log(response['msg'])
           }
         })
       },
       deleteBook(name){
       deletebook(this.output_bookname=name).then(response =>{
        if (response.error_num === 0){
             this.$message({'message':'删除客人成功',type:'success'})
             console.log(response['msg'])
             this.getList()
        }else{
             this.$message.error('删除客人信息失败，请重试')
             console.log(response['msg'])
             this.getList()
        }
        })
       },
       addUser() {
         addbook(this.input_bookname,this.input_money,this.input_address,this.input_relation,this.input_phone).then(response => {
           if (response.error_num === 0) {
             this.input_bookname = ''
             this.input_money = ''
             this.input_address = ''
             this.input_phone = ''
             this.input_relation = ''
             this.$message({'message':'新增客人成功',type:'success'})
             console.log(response['msg'])
             this.getList()
           } else {
             this.$message.error('新增客人信息失败，请重试')
             console.log(response['msg'])
           }
         })
       }
     }
   }
 </script>


<!--css部分-->
<style scoped lang="scss">
.dialog-demo {
  padding: 20px;
  .instructions {
    font-size: 14px;
    padding: 10px 0;
    color: #304455;
  }
  .desc-list {
    padding: 10px 0 30px 40px;
    line-height: 30px;
    font-size: 14px;
    color: #606266;
    list-style-type: disc;
  }
}
</style>
