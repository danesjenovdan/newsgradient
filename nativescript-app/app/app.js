import Vue from 'nativescript-vue';
import { Application } from '@nativescript/core';
import Pager from '@nativescript-community/ui-pager/vue';
import ImagePlugin from '@nativescript-community/ui-image/vue';
// eslint-disable-next-line import/no-unresolved
import { shutDown } from '@nativescript-community/ui-image';
import Home from './components/Home.vue';

Vue.use(Pager);
Vue.use(ImagePlugin);
Application.on(Application.exitEvent, () => shutDown());

new Vue({
  render: (h) => h('frame', [h(Home)]),
}).$start();
