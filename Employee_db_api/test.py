try:
    import unittest
    from app import app
    import  json

except Exception as e:
    print("somethig missing in code {}".format(e))

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()


    def test_employee_create(self):
        try:
            response = self.client.post("/empdb/employee/create", data=json.dumps({
                'Emp_id': '2342',
                'First_name': 'abc',
                'Last_name': 'sharma1',
                'Role': 'Junior Engineer'}),headers={"Content-Type": "application/json"})
            print(response.content_type)
            assert response.status_code == 200
            response_data=json.loads(response.get_data(as_text=True))
            print("employee create api method return",response_data )

        except Exception as e:
            print("somethig missing in code {}".format(e))

    def test_role_create(self):
        try:
            create_role_data = {
                'Role_id': '39',
                'Role_name': 'Senior Team Leader'
            }

            response = self.client.post("/rolesDB/Roles/create", data=json.dumps(create_role_data),headers={"Content-Type": "application/json"})
            print(response.content_type)
            assert response.status_code == 200
            self.assertEqual(response.content_type, "application/json")
            response_data = json.loads(response.get_data(as_text=True))
            print("Role create api method return", response_data)

        except Exception as e:
            print("somethig missing in code {}".format(e))

    def test_all_roles(self):
        try:

            response = self.client.post("/empdb/Roles", data={})
            print(response.content_type)

            assert response.status_code == 200
            self.assertEqual(response.content_type, "application/json")
            print("All Roles data API method return", response.get_data())

        except Exception as e:
            print("somethig missing in code {}".format(e))



    def test_employee_details(self):
        try:
            Emp_id= 201
            response = self.client.get("/empdb/employee/%s"%(Emp_id), data={})
            print(response)
            assert response.status_code == 200
            self.assertEqual(response.content_type, "application/json")
            print("Employee Details api method return values ", response.get_data())
        except Exception as e:
            print("somethig missing in code {}".format(e))


    def test_assign_role(self):
         try:
              Emp_id = 201
              assign_role_emp_data = {'Role': 'Technical specialist'}
              response = self.client.post("/empdb/employee/assignrole/%s"%(Emp_id),data=json.dumps(assign_role_emp_data),headers={"Content-Type": "application/json"})
              print(response)
              assert response.status_code == 200
              self.assertEqual(response.content_type, "application/json")
              role_response_data = json.loads(response.get_data(as_text=True))
              print("After Role assign updated api method return", role_response_data)
         except Exception as e:
            print("somethig missing in test_assign_role code {}".format(e))
    #
    def test_all_employee(self):
        try:
            response = self.client.post("/empdb/employees", data={})
            print(response)
            assert response.status_code == 200
            self.assertEqual(response.content_type, "application/json")
            print("All Employee api method return", response.get_data())
        except Exception as e:
            print("somethig missing in code {}".format(e))


    # check if the Response is 200
    def test_index_route(self):
        test_index = app.test_client(self)
        response=test_index.get("/")
        self.assertEqual(response.status_code,200)



if __name__ == '__main__':
    unittest.main()



