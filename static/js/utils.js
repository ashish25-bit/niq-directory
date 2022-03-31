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
