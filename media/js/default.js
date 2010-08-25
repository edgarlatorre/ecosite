function current(id) {	
	clear_all_menu();
	document.getElementById(id).setAttribute("class", "current_page_item");
}

function clear_all_menu() {
	alert("Limpando a casa")
	document.getElementById('home').removeAttribute("class");
	document.getElementById('about_we').removeAttribute("class");
	document.getElementById('contact').removeAttribute("class");
}