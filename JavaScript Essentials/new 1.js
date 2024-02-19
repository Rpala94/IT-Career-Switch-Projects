function myFunction () {
	var obj = document.getElementById("h01");
	obj.innerHTML = "Hello JQuery";
	}

function myFunction () {
	$("#h01").html("Hello JQuery");
}

$(document).ready(myFunction);