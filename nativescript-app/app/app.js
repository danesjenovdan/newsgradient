import Vue from 'nativescript-vue';
import Theme from '@nativescript/theme';
import Home from './components/Home.vue';
// import Event from './components/Event.vue';

Theme.setMode(Theme.Dark);
// Theme.setMode(Theme.Light);

new Vue({
  render: (h) => h('frame', [h(Home)]),
  // render: (h) => h('frame', [h(Event)]),
}).$start();
