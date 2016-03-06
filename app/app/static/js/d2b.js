Element.prototype.remove = function() {
    this.parentElement.removeChild(this);
}
NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
    for(var i = this.length - 1; i >= 0; i--) {
        if(this[i] && this[i].parentElement) {
            this[i].parentElement.removeChild(this[i]);
        }
    }
}

function initSearch(searchBox) {
	if(searchBox.value != "Sök på varg för bästa resultat...") return;
	searchBox.value = "";
	searchBox.classList.remove("fadedText");
}

function checkSearchInput(searchBox) {
	if(searchBox.value == "") {
		searchBox.value = "Sök på varg för bästa resultat...";
		searchBox.classList.add("fadedText");
	}
}

function searchClick(searchBox, e) {
	if(e.keyCode == 13) {
		document.getElementById("searchImg").click();	
	}
}

function search() {
	var searchBox = document.getElementById("searchTextInput");
	//window.location.href='/search.php?s=1&q=' + searchBox.value;
}

var oneProduct;
function columnCheckboxChanged(checkBox) {
    var data = document.getElementById("dataArea");
    var empty = data.childNodes[1].innerHTML === "";
    if(checkBox.checked) {
        data.childNodes[1].innerHTML += '<label style="display:block;" for="' + checkBox.id + '" class="' + checkBox.id + ';'+  checkBox.value + '">' + checkBox.id + '<input type="text" id="' + checkBox.id + '" /></label>';
        oneProduct = data.childNodes[1];
        var products = document.getElementsByClassName("product");
        for(var i = 0; i < products.length; i++) {
            products[i].innerHTML = oneProduct.innerHTML;
        }
    }
    else {
        var name = checkBox.id + ';' + checkBox.value;
        var products = document.getElementsByClassName(name).remove();
        oneProduct = data.childNodes[1];
    }
}


function addProduct() {
    var dataArea = document.getElementById("dataArea");
    dataArea.innerHTML += '<div class="product">' + oneProduct.innerHTML + '</div>';
}
