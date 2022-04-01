// runs when the page is loaded
window.addEventListener('load', () => {
  let temp = window.location.href.split('?')

  if (temp.length <= 1)
    return;

  temp = temp[1];
  temp = temp.split('&')

  let message = null;
  for (let i=0; i < temp.length; i++) {
    if (temp[i].includes('message')) {
      message = temp[i];
      break;
    }
  }

  if (message == null)
    return;

  message = message.split('=');
  if (message.length <= 1)
    return;

  message = message[1];
  message = message.split('-').join(' ');
  add_alert(message);
})