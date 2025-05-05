// M Yaqoob
#include <iostream>
#include <map>
using namespace std;

struct Employee
{
    string name;
    string dept;
    int salary;
};

void addEmmployee(map<int,Employee> &ems, int id, Employee employee){
    ems[id] = employee;
    cout << "Added Employee: ID " << id << ", Name: " << ems[id].name << ", Department: " << ems[id].dept << ", Salaray: "<< ems[id].salary << "\n"; 
}

void updateEmployee(map<int,Employee> &ems, int id, Employee employee){
    ems[id] = employee;
    cout << "Updated Employee: ID " << id <<  ", New Salaray: " << ems[id].salary << "\n"; 
}

void removeEmployee(map<int,Employee> &ems, int id){
    ems.erase(id);
    cout << "Removed Employee: ID " << id << "\n"; 
}
void displayEmployees(map<int, Employee> &ems){
    map<int, Employee>:: iterator iter = ems.begin();

    for (int i = 0; i < ems.size(); i++)
    {
        cout << i+ 1 << "." << " ID: " << iter->first << ", Name: " << iter->second.name << ", Department: " << iter->second.dept << ", Salaray: "<<iter->second.salary << "\n"; 
        *iter++;
    }

}

int main()
{
    map<int, Employee> ems;

    // employe 1
    Employee emplyee1;
    emplyee1.name = "Alice";
    emplyee1.dept = "HR";
    emplyee1.salary = 50000;
    addEmmployee(ems, 101, emplyee1);

    // employee 2
    Employee emplyee2;
    emplyee2.name = "Bob";
    emplyee2.dept = "Engineering";
    emplyee2.salary = 60000;
    addEmmployee(ems, 102, emplyee2);

    // update employee
    emplyee1.salary = 55000;
    updateEmployee(ems, 101, emplyee1);

    // remove employee
    removeEmployee(ems, 102);

    // dispaly all
    displayEmployees(ems);
    return 0;
}