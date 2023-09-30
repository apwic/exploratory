<template>
    <div id="app" class="small-container">
        <h1>Employee Table</h1>

        <employee-form @add:employee="addEmployee"></employee-form>
        <employee-table :employees="employees"></employee-table>
    </div>
</template>

<script>
import EmployeeTable from './components/EmployeeTable.vue';
import EmployeeForm from './components/EmployeeForm.vue';

export default {
    name: 'App',
    components: {
        EmployeeTable,
        EmployeeForm
    },
    methods: {
        addEmployee(employee) {
            const lastId =
                this.employees.length > 0
                    ? this.employees[this.employees.length - 1].id
                    : 0;
            const id = lastId + 1;
            const newEmployee = { ...employee, id };

            this.employees = [...this.employees, newEmployee];
        },
    },
    data() {
        return {
            employees: [
                {
                    id: 1,
                    name: 'Richard Hendricks',
                    email: 'richard@piedpiper.com',
                },
                {
                    id: 2,
                    name: 'Bertram Gilfoyle',
                    email: 'gilfoyle@piedpiper.com',
                },
                {
                    id: 3,
                    name: 'Dinesh Chugtai',
                    email: 'dinesh@piedpiper.com',
                },
            ],
        }
    },
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

button {
    background: #009435;
    border: 1px solid #009435;
}

.small-container {
    max-width: 680px;
}
</style>
