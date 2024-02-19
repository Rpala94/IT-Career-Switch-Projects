//console.log("This is an element of type: ", mainTitle.nodeType );
//console.log ("This inner HTML is ", mainTitle.innerHTML );
//console.log("There are this many child onjects ", mainTitle.childNodes );


//var myLinks = document.getElementsByTagName ("a");
//var firstLink = myLinks[0].getAttribute("href");
//console.log(firstLink);

//document.getElementById("mainTitle").innerHTML = "Why Travel with Us!"
//var align = mainTitle.getAttribute("align")
//console.log(align);

//document.getElementById("intro").style.backgroundColor = "yellow";
//document.getElementById("intro").style.fontFamily = "Times New Roman";

//document.getElementById ("customer1").setAttribute("style", "fontWeight:bold");

/*function simpleMessage () {
	alert("This is a simple alert box")
}

setTimeOut(simpleMessage, 5000);*/


var myImage = document.getElementById("Malaysia");

var imageArray = ["image/malaysia.jpg","images/malaysia2.jpg", "images/malaysia3.jpg","images/malaysia4.jpg" ];

var imageArray = 0;

function changeImage(){
	myImage,setAttribute("src", imageArray[imageIndex]);
	imageIndex++;
	if (imageIndex >= imageArray.length){
		imageIndex = 0;
	}
}

setInterval(changeImage, 5000);