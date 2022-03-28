// for removing the alert message container if present
async function setup() {
  const alertContainer = document.querySelector('.alert-message');
  if (!alertContainer)
    return;

  await sleep(5000)
  alertContainer.remove();
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

// calling functions
setup();
