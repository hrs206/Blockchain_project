const onCallRegister = async (email, name) => {
  try {
    const data = {
      email,
      name,
    };

    const response = await fetch(
      "https://mp-wallet-app-api.herokuapp.com/users",
      {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      }
    );

    const user = await response.json();
    return user;
  } catch (error) {
    return { error };
  }
};

const onCallLogin = async (email) => {
  try {
    const response = await fetch(
      `https://mp-wallet-app-api.herokuapp.com/users?email=${email}`
    );
    const user = await response.json();
    return user;
  } catch (error) {
    return { error };
  }
};

const onLogin = async () => {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if (email.length < 5 || !email.includes("@")) {
    alert("Invalid email");
    return;
  }

  const result = await onCallLogin(email);

  if (result.error) {
    alert("Failed to validate email.");
    return;
  }

  if (password === result.password) {
    localStorage.setItem("@WalletApp:userEmail", result.email);
    localStorage.setItem("@WalletApp:userName", result.name);
    localStorage.setItem("@WalletApp:userId", result.id);
    window.open("../home/index.html", "_self");
  } else {
    alert("Invalid password. Please try again.");
  }
};

const onRegister = async () => {
  const email = document.getElementById("input-email").value;
  const name = document.getElementById("input-name").value;

  if (name.length < 3) {
    alert("Name must contain more than 3 characters.");
    return;
  }

  if (email.length < 5 || !email.includes("@")) {
    alert("Invalid email");
    return;
  }

  const result = await onCallRegister(email, name);

  if (result.error) {
    alert("Failed to register.");
    return;
  }

  localStorage.setItem("@WalletApp:userEmail", result.email);
  localStorage.setItem("@WalletApp:userName", result.name);
  localStorage.setItem("@WalletApp:userId", result.id);
  window.open("signup_page/index.html", "_self");
};

window.onload = () => {
  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");

  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();
    onLogin();
  });

  registerForm.addEventListener("submit", (event) => {
    event.preventDefault();
    onRegister();
  });
};
