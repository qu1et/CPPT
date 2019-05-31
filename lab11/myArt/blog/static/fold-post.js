'use strict'

let foldBtns = document.getElementsByClassName("btn");

console.log(cont);

for (let i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        if (e.target.parentElement.className == "one-post folded") {
            e.target.innerHTML = "свернуть";
            e.target.parentElement.className = "one-post";
        }
        else {
            e.target.parentElement.className = "one-post folded";
            e.target.innerHTML = "развернуть";
        }
        console.log("you clicked", event.target);
    });

}
