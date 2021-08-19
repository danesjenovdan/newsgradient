import Theme from '@nativescript/theme';
// eslint-disable-next-line import/no-unresolved
import * as settings from '@nativescript/core/application-settings';

export function loadAndSetTheme() {
  if (settings.hasKey('dark-mode')) {
    Theme.toggleMode(settings.getBoolean('dark-mode', false));
  } else {
    Theme.setMode(Theme.Auto);
  }
}

export function toggleAndSaveTheme() {
  Theme.toggleMode();
  settings.setBoolean('dark-mode', Theme.getMode() === 'ns-dark');
}
