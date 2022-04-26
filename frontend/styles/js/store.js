let box = document.getElementById("store-items");

window.onload = function generate_default() {
    let load_amount = 49;
    for (let i = 0; i < load_amount; i++) {
        let newEle = document.createElement('div');
        let image_tag = document.createElement('div');
        image_tag.className = "img-temp";
        // image.innerHTML = "image"
        let image = document.createElement("img");
        image.src = "https://cdn11.bigcommerce.com/s-0ikue3/images/stencil/590x590/products/601/1346/CRPSN101__77504.1473186696.jpg?c=2";
        image_tag.appendChild(image)
        newEle.appendChild(image_tag);
        let product_info = document.createElement('div');
        product_info.className = "product-info"
        let product_name = document.createElement('h1');
        product_info.innerHTML = "PRODUCT NAME: "
        let product_price = document.createElement('p');
        product_price.innerHTML = "PRODUCT PRICE: ";
        let add_cart_btn = document.createElement("button");
        add_cart_btn.innerHTML = "ADD TO CART";
        add_cart_btn.className = "btn btn-primary";
        product_info.appendChild(product_name);
        product_info.appendChild(product_price);
        product_info.appendChild(add_cart_btn);
        newEle.appendChild(product_info);
        box.appendChild(newEle);
    }
    console.log("complete");
}

