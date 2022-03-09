const motds = [
    "now with 100% more javascript",
    "now with 200% more javascript",
    "now with 300% more javascript",
    "now with 400% more javascript",
    "scales well on mobile",
    "hitting 2 daily requests",
    "weezy as always",
    "may contain radium",
    "where dreams are made",
    "with cement and hookers",
    "with more than 280 characters",
    "best viewed in 4:3"
];

var motd = motds[Math.floor(Math.random() * motds.length)];
document.getElementById("motd-div").innerHTML = "<i>Random projects, thoughts, etc ... " + motd + '.</i>';

var home = document.getElementById("home-button-div");
var projects = document.getElementById("projects-button-div");
var movies = document.getElementById("movies-button-div");
var blog = document.getElementById("blog-button-div");
var links = document.getElementById("links-button-div");

home.innerHTML =
    "<button id=\"home-button\" class=\"top-links\"><img src=\"/img/catscape.gif\" width=15 height=15 class=\"icon\">Home</button>";
home.addEventListener("click", () => {
    window.location.href = "/index.html"
});

projects.innerHTML =
    "<button id=\"projects-button\" class=\"top-links\"><img src=\"/img/computer.gif\" width=15 height=15 class=\"icon\">Projects</button>";
projects.addEventListener("click", () => {
    window.location.href = "/projects.html"
});

movies.innerHTML =
    "<button id=\"movies-button\" class=\"top-links\"><img src=\"/img/cursor.gif\" width=15 height=15 class=\"icon\">Movies</button>";
movies.addEventListener("click", () => {
    window.location.href = "/movies.html"
});

blog.innerHTML =
    "<button id=\"blog-button\" class=\"top-links\"><img src=\"/img/documents.gif\" width=15 height=15 class=\"icon\">Blog</button>";
blog.addEventListener("click", () => {
    window.location.href = "/blog.html"
});

links.innerHTML =
    "<button id=\"links-button\" class=\"top-links\"><img src=\"/img/folder.gif\" width=15 height=15 class=\"icon\">Links</button>";
links.addEventListener("click", () => {
    window.location.href = "/links.html"
});

if (window.localStorage.getItem("theme") === "dark") document.body.classList.add("dark-no-trans");

document.getElementById("toggle-button").addEventListener("click", () => {
    if (window.localStorage.getItem("theme") === "dark") {
        window.localStorage.setItem("theme", "light");
        document.body.classList.remove("dark");
        document.body.classList.remove("dark-no-trans");
    } else {
        window.localStorage.setItem("theme", "dark");
        document.body.classList.remove("dark-no-trans");
        document.body.classList.add("dark");
    }
});
