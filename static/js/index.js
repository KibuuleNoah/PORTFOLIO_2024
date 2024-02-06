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

if (document.title !== "Home") {
  document.getElementById("cert-link").style.display = "none";
}

if (document.title === "Home") {
  main();

  let certToggler = document.getElementById("certToggler");
  certToggler.addEventListener("click", () => {
    if (certToggler.innerText == "More") {
      certToggler.innerText = "Less";
    } else {
      certToggler.innerText = "More";
    }
  });
}

String.prototype.toCamelCase = function () {
  return this.replace(/\w+/g, function (w) {
    return w[0].toUpperCase() + w.slice(1).toLowerCase();
  });
};

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

const validateEmailFormat = (email) =>
  /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(email);

//used to display error and success message to data input form
const flash = (node, message) => {
  // node.nextSibling.style.color = "red"
  node.nextSibling.textContent = message;
};

const clearFlashedMessages = (nodes) => {
  nodes.forEach((node) => {
    node.nextSibling.textContent = "";
  });
};

const validateContactForm = () => {
  let form = document.forms["contact-form"];
  let name = form["name"];
  let email = form["email"];
  let message = form["message"];

  clearFlashedMessages([name, email, message]);
  if (!name.value) {
    flash(name, "Name field is empty");
  } else if (!email.value) {
    flash(email, "Email field is empty");
  } else if (!message.value) {
    flash(message, "Message field is empty");
  } else if (!validateEmailFormat(email.value)) {
    flash(email, "Invalid Email format");
  } else {
    let data = { name: name.value, email: email.value, message: message.value };
    fetch("/contact-me", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });
    document.getElementById("thanks").innerHTML =
      `Thank you so much <b>${name.value.toCamelCase()}</b> for taking the time to explore my portfolio and send me a message.`;

    name.value = "";
    email.value = "";
    message.value = "";
    "noah".toCamelCase();
    const toastLiveExample = document.getElementById("liveToast");
    const toastBootstrap =
      bootstrap.Toast.getOrCreateInstance(toastLiveExample);
    toastBootstrap.show();
  }
};
