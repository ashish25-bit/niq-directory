const deleteBtns = document.querySelectorAll('[data-id]')

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

deleteBtns.forEach(btn => {
  btn.addEventListener('click', async e => {
    if (!confirm('Confirm to delete'))
      return;

    const id = e.target.dataset.id;
    const parent = e.target.parentElement;
    e.target.disabled = true;

    fetch(`http://localhost:8000/delete?method=DELETE&id=${id}`)
      .then(res => {
        if (isJSONSafe(res))
          return res.json();

        return res.text();
      })
      .then(res => {
        add_alert(res);
        parent.remove();
      })
      .catch(err => {
        add_alert('Error in deleting employee');
        console.log(err);
      })
  })
})
