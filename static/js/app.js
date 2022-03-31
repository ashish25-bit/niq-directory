const deleteBtns = document.querySelectorAll('[data-name]')

// for removing the alert message container if present
async function remove_alert_container() {
  const alertContainer = document.querySelector('.alert-message');
  if (!alertContainer)
    return;

  await sleep(5000)
  alertContainer.remove();
}

function add_alert(text) {
  const div = document.createElement('div');
  div.classList.add('alert-message');
  div.innerText = text;
  document.body.append(div);
  remove_alert_container();
}

function isJSONSafe(data) {
  try {
    JSON.parse(data);
    return true;
  }
  catch (_) {
    return false;
  }
}

function sleep(time = 1000) {
  return new Promise(resolve => {
    setTimeout(resolve, time);
  })
}

deleteBtns.forEach(btn => {
  btn.addEventListener('click', async e => {
    if (!confirm('Confirm to delete'))
      return;

    const name = e.target.dataset.name;
    const parent = e.target.parentElement;
    e.target.disabled = true;

    await sleep(5000)

    fetch(`http://localhost:8000/delete?method=DELETE&name=${name}`)
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

// calling functions
remove_alert_container();
