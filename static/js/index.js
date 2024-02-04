const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    }
    // else {
    // entry.target.classList.remove("show");
    // }
  });
});

const hiddenElems = document.querySelectorAll("section");
hiddenElems.forEach((el) => observer.observe(el));

if (document.title === "Home") {
  main();
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function typewrite(txt, el) {
  el.innerText = "";
  for (const char of txt) {
    el.textContent += char;
    await sleep(100);
  }
}

async function typewrite2(txt, el) {
  for (const char of txt) {
    el.textContent = el.textContent.slice(0, -1);
    await sleep(250);
  }
}

async function main() {
  const TAILS = [
    "SOFTWARE DEVELOPER",
    "PROGRAMMER",
    "SYSTEM DESIGNER",
    "BACKEND DESIGNER",
    "SKILLED FREELACER",
  ];
  const tail = document.querySelector(".tail");
  let tailIndex = 0;
  while (true) {
    await typewrite(TAILS[tailIndex], tail);
    await sleep(1000);
    await typewrite2(TAILS[tailIndex], tail);
    await sleep(1000);
    tailIndex = (tailIndex + 1) % TAILS.length;
  }
}

/*
 * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
.display {
    box-shadow: 0 0 2px 2px pink;
    padding: 1rem;
    border-radius: 5px;
  }

#btn {
    padding: 30px;
    border-radius: 6px;
    left: 50px;
    position: absolute;
    cursor: pointer;
}

<body>
    <button id="btn" type="button">Type</button>
    <div class="display">
        <span class="root"></span>
        <span class="tail"></span>
    </div>
</body>
 */
