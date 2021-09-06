let componentListenerFunction = null;

function onMessageReceivedCallback(message) {
  // eslint-disable-next-line no-console
  console.log(`message: ${JSON.stringify(message, null, 2)}`);

  if (message.foreground) {
    if (typeof componentListenerFunction === 'function') {
      componentListenerFunction(message);
    }
  }
}

export const firebaseInitParams = {
  onMessageReceivedCallback,
  // foreground notifications only work on iOS with this enabled,
  // in android you have to open a notification manually if in foreground
  // showNotificationsWhenInForeground: true,
};

export function setMessageReceivedListener(func) {
  componentListenerFunction = func;
}
