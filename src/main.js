import { createApp } from 'vue'
import App from './App.vue'
import { createStore } from 'vuex'

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(fas)

// 创建 Vuex store
const store = createStore({
  state() {
    return {
      searchQuery: ''
    }
  },
  mutations: {
    updateSearchQuery(state, query) {
      state.searchQuery = query;
    }
  }
})

const app = createApp(App)

app.use(store) // 使用 Vuex store

app.component('font-awesome-icon', FontAwesomeIcon)

app.mount('#app')