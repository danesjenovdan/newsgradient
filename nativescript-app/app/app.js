import Vue from 'nativescript-vue';
import { Application } from '@nativescript/core';
// eslint-disable-next-line import/no-unresolved
import { firebase } from '@nativescript/firebase';
import Pager from '@nativescript-community/ui-pager/vue';
import ImagePlugin from '@nativescript-community/ui-image/vue';
// eslint-disable-next-line import/no-unresolved
import { shutDown } from '@nativescript-community/ui-image';
import { firebaseInitParams } from './services/notifications.service';
import Home from './components/Home.vue';

firebase.init({ ...firebaseInitParams });

firebase.getCurrentPushToken().then((token) => {
  // eslint-disable-next-line no-console
  console.log(`push token: ${token}`);
});

Vue.use(Pager);
Vue.use(ImagePlugin);
Application.on(Application.exitEvent, () => shutDown());

new Vue({
  render: (h) => h('frame', [h(Home)]),
}).$start();
