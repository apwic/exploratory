<template>
    <div id="employee-form">
        <form @submit.prevent="handleSubmit">
            <label>Employee Name</label>
            <input
                ref="first"
                type="text" 
                v-model="employee.name" 
                :class="{ 'has-error': submitting && invalidName }"
                @focus="clearStatus" 
                @keypress="clearStatus"
            />
            <label>Employee Email</label>
            <input
                type="text" 
                v-model="employee.email" 
                :class="{ 'has-error': submitting && invalidEmail }"
                @focus="clearStatus" 
            />
            <button>Add Employee</button>
            <p v-if="error && submitting" class="error-message">❗Please fill out all required fields</p>
            <p v-if="success" class="success-message">✅ Employee successfully added</p>
        </form>
    </div>
</template>

<script>
export default {
    name: 'employee-form',
    computed: {
        invalidName() {
            return this.employee.name === ''
        },
        invalidEmail() {
            return this.employee.email === ''
        },
    },
    data() {
        return {
            submitting: false,
            error: false,
            success: false,
            employee: {
                name: '',
                email: '',
            },
        }
    },
    methods: {
        handleSubmit() {
            this.submitting = true
            this.clearStatus()

            if (this.invalidName || this.invalidEmail) {
                this.error = true
                return
            }

            this.$emit('add:employee', this.employee)
            this.$refs.first.focus()
            this.employee = {
                name: '',
                email: ''
            }
            this.error = false
            this.success = true
            this.submitting = false
        },
        clearStatus() {
            this.success = false
            this.error = false
        },
    },
};
</script>

<style scoped>
form {
    margin-bottom: 2rem;
}

[class*='-message'] {
    font-weight: 500;
}

.error-message {
    color: #d33c40;
}

.success-message {
    color: #32a95d;
}
</style>