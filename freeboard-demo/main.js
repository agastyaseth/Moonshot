inputId = document.getElementById('from');
inputId.addEventListener('keyup', function onEvent(e) {
    if (e.keyCode ==13) {
       
       var loc = document.getElementById("from").value;
       console.log(loc);
       var urlof = "http://www.mapquestapi.com/geocoding/v1/address?key=NG1xUa3X72GluOBcL25KxH33XZq40O9Z&location=";
       var keywords = loc.split(" ");
       for(var i=0;i<keywords.length-1;++i)
       {
        urlof = urlof+keywords[i]+"%20";
       }
       urlof = urlof + keywords[keywords.length-1];
       console.log(urlof)
    //    var ourRequest = new XMLHttpRequest();
    //    ourRequest.open('GET', url);
    //    ourRequest.onload = function() {
    //    var ourData = JSON.parse(ourRequest.responseText);
    //   }
    // ourRequest.send();   
      $.ajax({
        type: 'GET',
        url: urlof,
        success: function(data)
        {
          console.log(data);
          if(data!=undefined)
          document.getElementById("from").value = data["results"][0]["locations"][0]["latLng"]["lat"];
        }
      })
  }
});

inputId = document.getElementById('to');
inputId.addEventListener('keyup', function onEvent(e) {
    if (e.keyCode ==13) {
       
       var loc = document.getElementById("to").value;
       console.log(loc);
       var urlof = "http://www.mapquestapi.com/geocoding/v1/address?key=NG1xUa3X72GluOBcL25KxH33XZq40O9Z&location=";
       var keywords = loc.split(" ");
       for(var i=0;i<keywords.length-1;++i)
       {
        urlof = urlof+keywords[i]+"%20";
       }
       urlof = urlof + keywords[keywords.length-1];
       console.log(urlof)
    //    var ourRequest = new XMLHttpRequest();
    //    ourRequest.open('GET', url);
    //    ourRequest.onload = function() {
    //    var ourData = JSON.parse(ourRequest.responseText);
    //   }
    // ourRequest.send();   
      $.ajax({
        type: 'GET',
        url: urlof,
        success: function(data)
        {
          console.log(data);
          if(data!=undefined)
          document.getElementById("to").value = data["results"][0]["locations"][0]["latLng"]["lat"];
        }
      })
  }
});
