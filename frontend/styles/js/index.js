console.log("Working");

let helper = document.getElementById("search-by-helper");

let brands = ["NIKE", "ADIDAS"];
let categories = ["Clothes", "Shoes"]
let prices = ["$20", "$40", "$60", "$80", "$100", "$120", "$140", "$160", "$180", "+$200"]

function searchBy(event) {
    if (helper.childElementCount > 0) {
        searchByRemover();
    }

    let id = event.target.id;
    list = [];
    if (id == "brand") {
        for (let i = 0; i < brands.length; i++) {
            list[i] = brands[i];
        }
    }
    else if (id == "categories") {
        for (let i = 0; i < categories.length; i++) {
            list[i] = categories[i];
        }
    }
    else if (id == "prices") {
        for (let i = 0; i < prices.length; i++) {
            list[i] = prices[i];
        }
    }

    console.log(id, list)

    for (let i = 0; i < list.length; i++) {
        let newEle = document.createElement('div');
        newEle.innerHTML = list[i];
        newEle.className = "search-by";
        newEle.nodeName = "dynamic"
        helper.appendChild(newEle);
    }
}

function searchByRemover() {
    while (helper.firstChild){
        helper.removeChild(helper.firstChild);
    }
}

window.onload = function generate_default() {
    let load_amount = 49;
    let box = document.getElementById("layout");
    for (let i = 0; i < load_amount; i++) {
        let newEle = document.createElement('div');
        newEle.className = "item";
        newEle.innerHTML = "default";
        box.appendChild(newEle);
    }
    console.log("complete");
}

var dropdown = document.getElementsByClassName("brand-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

var dropdown = document.getElementsByClassName("category-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

var dropdown = document.getElementsByClassName("price-range-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

