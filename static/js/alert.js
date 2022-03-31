// for removing the alert message container if present
async function remove_alert_container(container) {
  if (!container)
    return;

  await sleep(5000)
  container.remove();
}

function add_alert(text) {
  const div = document.createElement('div');
  div.classList.add('alert-message');
  div.innerText = text;
  document.body.append(div);
  remove_alert_container(div);
}