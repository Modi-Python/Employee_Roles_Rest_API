from flask import Flask
from flask import jsonify
from flask import request
import datetime
app = Flask(__name__)



rolesDB=[
    {
        'Role_id': '1',
        'Role_name': 'Technical Leader',

    },
    {
        'Role_id': '2',
        'Role_name': 'Team Leader',

    },
    {
        'Role_id': '3',
        'Role_name': 'Project Leader',

    }

]
empDB = [
    {
        'Emp_id': '101',
        'First_name': 'Saravanan S',
        'Last_name': 'Murthy',
        'Role': 'Technical Leader'
    },
    {
        'Emp_id': '201',
        'First_name': 'Raj S',
        'Last_name': 'Kumar',
        'Role': 'Sr Software Engineer'
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print("Welcome to REST API Testing")
        return "POST method called"

    return "GET method called"

@app.route('/empdb/employees', methods=['GET','POST'])
def getAllEmp():
    return jsonify({'emps': empDB})


@app.route('/empdb/Roles', methods=['GET','POST'])
def getAllRoles():
    return jsonify({'Roles': rolesDB})

@app.route('/empdb/employee/<empId>',methods=['GET'])
def getEmpDetails(empId):
    usr = [emp for emp in empDB if (emp['Emp_id'] == empId)]
    return jsonify({'emp': usr})

@app.route('/empdb/employee/create', methods=['POST'])
def createEmp():
    try:
        print("before insert", empDB)
        #
        # Test_emp = {
        #     'Emp_id': request.form.get('Emp_id'),
        #     'First_name': request.form.get('First_name'),
        #     'Last_name': request.form.get('Last_name'),
        #     'Role': request.form.get('Role'),
        # }
        temp_data=request.get_json()
        # print("request json",temp_data)
        Test_emp = {
            'Emp_id': temp_data['Emp_id'],
            'First_name': temp_data['First_name'],
            'Last_name': temp_data['Last_name'],
            'Role': temp_data['Role'],
        }
        empDB.append(Test_emp)
        print("after empDB", empDB)
        return jsonify({'emps': empDB})

    except Exception as e:
        print("somethig missing in create emp code {}".format(e))


@app.route('/rolesDB/Roles/create', methods=['POST'])
def createRole():
    try:
            print("before insert", rolesDB)
            temp_role_data = request.get_json()
            Test_Role = {
                'Role_id': temp_role_data['Role_id'],
                'Role_name': temp_role_data['Role_name']}
            rolesDB.append(Test_Role)
            print("after rolesDB", rolesDB)
            return jsonify({'Roles': rolesDB})

    except Exception as e:
        print("somethig missing in create Role code {}".format(e))




@app.route('/empdb/employee/assignrole/<empId>', methods=['GET','POST'])
def assign_role_Emp(empId):
    try:
        print("before update all employees ", empDB)
        em = [emp for emp in empDB if (emp['Emp_id'] == empId)]
        print("em values", em)
        print("request.json values is", request)
        temp_role_assign_data = request.get_json()
        if 'Role' in temp_role_assign_data:
            em[0]['Role'] = temp_role_assign_data['Role']
        return jsonify({'emp': em[0]})

    except Exception as e:
        print("somethig issues assign_role_Emp code {}".format(e))




if __name__ == '__main__':
    app.run()


