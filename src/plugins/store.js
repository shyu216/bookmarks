// plugins/store.js
import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      searchQuery: ''
    };
  },
  mutations: {
    updateSearchQuery(state, query) {
      state.searchQuery = query;
    }
  }
});

export default store;