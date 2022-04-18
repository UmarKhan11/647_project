let box = document.getElementById("cart-items");

window.onload = function generate_default() {
    let load_amount = 5;
    for (let i = 0; i < load_amount; i++) {
        let newEle1 = document.createElement('div');
        newEle1.className = "cart-card";
        let newEle2 = document.createElement('div');
        newEle2.className = "card-format";
        newEle2.innerHTML = "CART_ID";
        let newEle3 = document.createElement('div');
        newEle3.className = "card-format";
        newEle3.innerHTML = "USERNAME";
        let btn = document.createElement('button');
        btn.className = "card-format btn btn-primary";
        btn.innerHTML = "VIEW CART";
        newEle1.appendChild(newEle2);
        newEle1.appendChild(newEle3);
        newEle1.appendChild(btn);
        box.appendChild(newEle1);
    }
    console.log("complete");
}