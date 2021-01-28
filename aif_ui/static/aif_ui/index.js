/* When the user clicks on the button, toggle between hiding and showing the dropdown content */
function show_character_menu() {
	document.getElementById("character_menu").classList.toggle("show");
}

/* When the user clicks on the button, toggle between hiding and showing the dropdown content */
function show_user_menu() {
	document.getElementById("user_menu").classList.toggle("show");
}


/* popup a dialog for things that aren't implemented yet */
function doesNothing(msg) {
	alert(msg + " doesn't do anything yet");
}

function showLogin() {
	document.getElementById("modal_popup").style.display = "block";
}

function closeLogin() {
	document.getElementById("modal_popup").style.display = "none";
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

function XshowCharacter() {
	var x = document.getElementById("open_char").value;
	var y = "{% url 'character' 'Value' %}".replace("Value", x)
	window.location.href=y;
}

/* window.onclick = function(event) {
} */
