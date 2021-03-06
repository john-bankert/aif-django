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

function loadCharacterSheet(evt, csrf, sheet) {
	var i, tab_links;
	tab_links = document.getElementsByClassName("tablinks");
	for (i = 0; i < tab_links.length; i++) {
		tab_links[i].className = tab_links[i].className.replace(" active", "");
	}
	if (sheet == 'Combat') {
    //    $('#edit_button').hide()
	//   document.getElementById("edit_button").disabled = true;
	   $('#edit_button').disabled = true;
	} else {
	//    $('#edit_button').show()
    //    document.getElementById("edit_button").disabled = false;
	    $('#edit_button').disabled = false;
	}
	evt.currentTarget.className += " active";
	$.ajax({
		type: "POST",
		url: '/load-character-sheet/',
		data: { csrfmiddlewaretoken: csrf, sheet_id: sheet },
		success: function (data) { $('.tab_content').html(data); },
    });
	if (sheet == 'Combat') {
	   document.getElementById("edit_button").disabled = true;
	//   $('#edit_button').disabled = true;
	} else {
	    document.getElementById("edit_button").disabled = false;
	//    $('#edit_button').disabled = false;
	}
}

function editCharacterSheet(evt, csrf) {
    $('#edit_button').hide()
    $('#save_button').show()
 	$.ajax({
		type: "POST",
		url: '/edit-character-sheet/',
		data: { csrfmiddlewaretoken: csrf},
		success: function (data) { $('.tab_content').html(data); },
    });
}

function saveCharacterSheet(evt, csrf) {
    $('#save_button').hide()
    $('#edit_button').show()
    $('character_form').submit()
    //this.form.submit()
}

function hiThere() { alert('hi there'); }
//$(function() {
//    $("#edit_button").click(function() {
//      alert( "Handler for .click() called." );
//    });
//});