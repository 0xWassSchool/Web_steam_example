if (localStorage.getItem("auth") === null) {
    alert("You are not authtenticated");

    return window.location.href = "/admin/login";
}

