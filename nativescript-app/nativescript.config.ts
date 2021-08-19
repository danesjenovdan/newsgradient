import { NativeScriptConfig } from '@nativescript/core';

export default {
  id: 'si.danesjenovdan.newsgradient',
  appPath: 'app',
  appResourcesPath: 'App_Resources',
  android: {
    v8Flags: '--expose_gc',
    markingMode: 'none'
  }
} as NativeScriptConfig;
