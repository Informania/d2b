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
	window.location.href='/search.php?s=1&q=' + searchBox.value;
}
