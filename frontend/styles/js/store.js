let box = document.getElementById("store-items");

window.onload = function generate_default() {
    let load_amount = 49;
    for (let i = 0; i < load_amount; i++) {
        let newEle = document.createElement('div');
        newEle.innerHTML = "default";
        box.appendChild(newEle);
    }
    console.log("complete");
}

