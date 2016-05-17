//Element.prototype.remove = function() {
//    this.parentElement.removeChild(this);
//}
//NodeList.prototype.remove = HTMLCollection.prototype.remove = function() {
//    for(var i = this.length - 1; i >= 0; i--) {
//        if(this[i] && this[i].parentElement) {
//            this[i].parentElement.removeChild(this[i]);
//        }
//    }
//}

$(document).ready(function() {
	var buttons = document.getElementsByClassName("imageSizeButton");
	$(buttons[0]).addClass("inactive");
	var curSize = $('#currentImageSize').html();
	for(var i = 0; i < buttons.length; i++) {
		$(buttons[i]).on("click", function() {
			switch(this.innerHTML) {
				case "-":
					if(curSize == 4) return;
					
					curSize++;
					if(curSize == 4)
						$(buttons[0]).addClass("inactive");
					if(curSize > 2) 
						$(buttons[1]).removeClass("inactive");

					$('.card').removeClass('card-2').removeClass('card-3').removeClass('card-4').addClass('card-'+curSize);
					break;
				case "+":
					if(curSize == 2) return;
					
					curSize--;
					if(curSize == 2)
						$(buttons[1]).addClass("inactive");
					if(curSize < 4) 
						$(buttons[0]).removeClass("inactive");

					$('.card').removeClass('card-2').removeClass('card-3').removeClass('card-4').addClass('card-'+curSize);
					break;
			}

		});
	}
	$("#productGroupsNav").on("click", function () {
		var nav = $("#productGroupsNavInner");
		var triangle = $("#navTriangle");
		if(nav.hasClass('hidden')) {
			nav.removeClass('hidden');
			triangle.html('&#x25B2;');
		}
		else {
			nav.addClass('hidden');
			triangle.html('&#x25BC;');
		}
	});
})

function initSearch(searchBox) {
	if(searchBox.value != "Sök produkt") return;
	searchBox.value = "";
	searchBox.classList.remove("fadedText");
}

function checkSearchInput(searchBox) {
	if(searchBox.value == "") {
		searchBox.value = "Sök produkt";
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
	window.location.href='/sok/' + searchBox.value;
}
/* Code for adding product. Scrap atm. 
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
} */
