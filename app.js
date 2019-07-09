var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var methodOverride = require("method-override")
var jsdom = require('jsdom');
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;

var src,dst;
var $ = jQuery = require('jquery')(window);

app.use(express.static('public'))
app.use(methodOverride("_method"));
app.use(bodyParser.urlencoded({extended:true}));


app.get("/",function(req,res){
	res.render("start.ejs");
});



app.post("/details",function(req,res){
	console.log(req.body);
       var loc = req.body.fname;
       var urlof = "http://www.mapquestapi.com/geocoding/v1/address?key=NG1xUa3X72GluOBcL25KxH33XZq40O9Z&location=";
       var keywords = loc.split(" ");
       for(var i=0;i<keywords.length-1;++i)
       {
        urlof = urlof+keywords[i]+"%20";
       }
       urlof = urlof + keywords[keywords.length-1];
       console.log(urlof)
      $.ajax({
        type: 'GET',
        url: urlof,
        success: function(data)
        {
          console.log(data["results"][0]["locations"][0]["latLng"]["lat"]);
          src = data["results"][0]["locations"][0]["adminArea5"];
          console.log(src);
          // $("#from").html(src);
        }
      })

      var loc = req.body.lname;
       var urlof = "http://www.mapquestapi.com/geocoding/v1/address?key=NG1xUa3X72GluOBcL25KxH33XZq40O9Z&location=";
       var keywords = loc.split(" ");
       for(var i=0;i<keywords.length-1;++i)
       {
        urlof = urlof+keywords[i]+"%20";
       }
       urlof = urlof + keywords[keywords.length-1];
       console.log(urlof)
      $.ajax({
        type: 'GET',
        url: urlof,
        success: function(data)
        {
          console.log(data["results"][0]["locations"][0]["latLng"]["lat"]);
          dst = data["results"][0]["locations"][0]["adminArea5"];
          console.log(dst);
          // $("#to").html(dst);
          res.redirect("/final");
        }
      });
		// res.render("index.ejs",{from:src,to:dst});
});
app.get("/final",function(req,res){
	res.render("index.ejs",{from:src,to:dst});

})
app.listen(3000,function(){
	console.log("Server started");
});










