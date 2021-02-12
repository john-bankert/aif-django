/* When the user clicks on the button, toggle between hiding and showing the dropdown content */
function show_menu(menu_name) {
	document.getElementById(menu_name).classList.toggle("show");
}

/* popup a dialog for things that aren't implemented yet */
function doesNothing(msg) {
	alert(msg + " doesn't do anything yet");
}

function showPopup(popup_name) {
	document.getElementById(popup_name).style.display = "block";
}

function closePopup(popup_name) {
	document.getElementById(popup_name).style.display = "none";
}

/* Close the dropdown if the user clicks outside of it */
window.onclick = function(event) {
	if (!event.target.matches('.menu_icon')) {
		/* check to see if character_menu is visible */
		var characterMenu = document.getElementById("character_menu");
		if (characterMenu.classList.contains('show')) {
			characterMenu.classList.remove('show');
		}
		/* check to see if user_menu is visible */
		var userMenu = document.getElementById("user_menu");
		if (userMenu.classList.contains('show')) {
			userMenu.classList.remove('show');
		}
		/* var modal = document.getElementById("modal_popup");
		if (event.target == modal) {
			modal.style.display = "none";
		} */
	}
}

function showCharacter() {
	var x = document.getElementById("open_char").value;
	//var y = "{% url '/character' 'Value' %}".replace("Value", x)
	var y = "/character/Value".replace("Value", x)
	window.location.href=y;
}

function loadCharacterSheet(evt, name, sheet, theme) {
	var i, tab_links;
	tab_links = document.getElementsByClassName("tablinks");
	for (i = 0; i < tab_links.length; i++) {
		tab_links[i].className = tab_links[i].className.replace(" active", "");
	}
	evt.currentTarget.className += " active";

	$.ajax({
		type: "POST",
		url: '{{ '/load-character-sheet/' }}',
		data: { csrfmiddlewaretoken: '{{ csrf_token }}', character_name: name, sheet_id: sheet, current_theme: theme },
		success: function (data) { $('.tabcontent').html(data); }
	});
}