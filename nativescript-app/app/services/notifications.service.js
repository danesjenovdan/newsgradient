function onMessageReceivedCallback(message) {
  // eslint-disable-next-line no-console
  console.log(`message: ${JSON.stringify(message, null, 2)}`);
}

// eslint-disable-next-line import/prefer-default-export
export const firebaseInitParams = {
  onMessageReceivedCallback,
  showNotificationsWhenInForeground: true,
};
