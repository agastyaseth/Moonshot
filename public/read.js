console.log("I'm here");
function FetchData() {
const Http = new XMLHttpRequest();
const url='http://localhost:3000/return';
Http.open("GET", url);
Http.send();

	Http.onreadystatechange = function(){
		if(this.readyState==4 && this.status==200)
		{

			console.log(Http.responseText);
			var x = document.getElementById("battery"); 
			if(x!=null)
				x.textContent = "SexyBitch"
		}
	}
}
setInterval(FetchData, 2000);