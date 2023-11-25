function callFunction(n) {
  // /call_function/${Number}: This constructs a URL
  // The fetch() function is a modern web API used for making HTTP requests. It initiates a GET request to the specified URL.
  // fetch(`/call_function/${Number}`)
  //   .then(response => response.text())
  //   .then(data => {
  //     console.log(data);
  //   });
  switch(n){
    case 1:
      fetch(`/forward`);
      document.getElementById('content').innerText = "forward";
      break;
    case 2:
      fetch(`/backward`);
      document.getElementById('content').innerText = "backward";
      break;
    case 3:
      fetch(`/left`);
      document.getElementById('content').innerText = "left";
      break;
    case 4:
      fetch(`/right`);
      document.getElementById('content').innerText = "right";
      break;
    case 5:
      fetch(`/stop`);
      document.getElementById('content').innerText = "stop";
      break;
  }
}

let isUpArrowPressed = false;
let isDownArrowPressed = false;
let isLeftArrowPressed = false;
let isRightArrowPressed = false;


document.addEventListener('keydown', function (event) {
  switch (event.key) {
    case 'ArrowUp':
      isUpArrowPressed = true;
      callFunction(1);
      break;
    case 'ArrowDown':
      isDownArrowPressed = true;
      callFunction(2);
      break;
    case 'ArrowLeft':
      isLeftArrowPressed = true;
      callFunction(3);
      break;
    case 'ArrowRight':
      isRightArrowPressed = true;
      callFunction(4);
      break;
  }
});

document.addEventListener('keyup', function (event) {
  switch (event.key) {
    case 'ArrowUp':
      isUpArrowPressed = false;
      callFunction(5);
      break;
    case 'ArrowDown':
      isDownArrowPressed = false;
      callFunction(5);
      break;
    case 'ArrowLeft':
      isLeftArrowPressed = false;
      callFunction(5);
      break;
    case 'ArrowRight':
      isRightArrowPressed = false;
      callFunction(5);
      break;
  }
});