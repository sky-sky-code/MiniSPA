import Vue from 'vue';
import Router from 'vue-router';
import MiniSPA from '@/components/MiniSPA';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MiniSPA',
      component: MiniSPA,
    },
  ],
  mode: 'history',
});
