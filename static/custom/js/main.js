const accordionBtns = document.querySelectorAll(".accordion");

accordionBtns.forEach((accordion) => {
    accordion.onclick = function() {
        this.classList.toggle("is-open");

        let content = this.nextElementSibling;
        console.log(content);

        if (content.style.maxHeight) {
            //this is if the accordion is open
            content.style.maxHeight = null;
        } else {
            //if the accordion is currently closed
            content.style.maxHeight = content.scrollHeight + "px";
            console.log(content.style.maxHeight);
        }
    };
});

//sidenav

var width, height;
window.onresize = window.onload = function() {
    w = this.innerWidth;
    if (w > 1000) {
        closeNav();
        console.log(w);
    }

}

function openNav() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("mySidebar").style.position = "fixed";
    document.getElementById("mySidebar").style.zIndex = "100";
    document.getElementById("mySidebar").style.width = "40vw";
}

function closeNav() {
    document.getElementById("mySidebar").style.display = "none";
}