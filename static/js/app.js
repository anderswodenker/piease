const load = () => {

};

window.onload = load;

// vue.js
const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],


    data() {
        return {
            showMenu: false,
            greeting: 'Hello, Vue!',
            chosen_one: {'name': ''},
            sex: "",
            char: "",
            pet: "",
            input_error: '',
            system_error: '',
            tel: '+49 01577 36 13 245',
            ad_mail: "ad@pet-name-generator.com",
            contact_mail: 'contact@pet-name-generator.com',
            content_list: [],
            statistics: ''
        }
    },
    mounted() {
        this.get_api('/api/get_statistics', 'statistics')
    },

    methods: {
        get_api(url, api_type) {
            console.log(url)
            let that = this;
            axios.get(url).then((response) => {
                console.log(response.data)
                if (api_type === 'content') {
                    that.content_list = response.data

                }
                if (api_type === 'statistics') {
                    that.statistics = response.data
                }
            })
                .catch(function (error) {
                    console.log(error)
                    that.system_error = error;

                });
        },
        post_change_content(data) {
            let that = this;
            axios.post('/api/change_content', {
                data: data
            })
                .then(function (response) {
                    that.get_api('/api/get_content', 'content')
                    that.get_api('/api/get_statistics', 'statistics')
                })
                .catch(function (error) {
                    console.log(error)
                    that.system_error = error;

                });
        },
        change_content(tag, val, name) {
            let that = this;
            let data;
            if (tag === "sex") {
                this.sex = val
                data = {"$set": {'name': name, sex: val}}
            }
            if (tag === "char") {
                this.char = val
                data = {"$set": {'name': name, char: val}}
            }
            if (tag === "pet") {
                this.pet = val
                data = {"$set": {'name': name, pet: val}}
            }
            this.post_change_content(data)


        },
        click_tags(tag, val) {
            if (tag === "sex") {
                this.sex = val
            }
            if (tag === "char") {
                this.char = val
            }
            if (tag === "pet") {
                this.pet = val
            }
        },
        find_names() {
            if (this.sex || this.char || this.pet) {
                this.input_error = ''
                let that = this;
                axios.post('/api/query_name', {
                    sex: this.sex,
                    char: this.char,
                    pet: this.pet
                })
                    .then(function (response) {
                        const name = response.data[Math.floor(Math.random() * response.data.length)];
                        (name) ? that.chosen_one = name : that.chosen_one = '';
                    })
                    .catch(function (error) {
                        that.system_error = error;

                    });
            } else {
                this.input_error = 'Click at least on one tag please? :)'
            }
        }
    }
});