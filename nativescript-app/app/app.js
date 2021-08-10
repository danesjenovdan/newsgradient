import Vue from 'nativescript-vue';
import Theme from '@nativescript/theme';
import { Application } from '@nativescript/core';
// eslint-disable-next-line import/no-unresolved
import { shutDown } from '@nativescript-community/ui-image';
import ImagePlugin from '@nativescript-community/ui-image/vue';
import Home from './components/Home.vue';

Vue.use(ImagePlugin);
Application.on(Application.exitEvent, () => shutDown());

Theme.setMode(Theme.Dark);
// Theme.setMode(Theme.Light);

new Vue({
  render: (h) => h('frame', [h(Home)]),
}).$start();
