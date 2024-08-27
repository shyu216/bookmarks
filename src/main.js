import { createApp } from 'vue'
import App from './App.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import vuetify from './plugins/vuetify'
import store from './plugins/store'

library.add(fas)

const app = createApp(App)

app.use(store) // 使用 Vuex store

app.use(vuetify) // 使用 Vuetify

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')