const deleteBtns = document.querySelectorAll('[data-id]')

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
