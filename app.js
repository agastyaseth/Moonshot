var express = require("express");
var app = express();
var bodyParser = require("body-parser");
var methodOverride = require("method-override")
var jsdom = require('jsdom');
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;

const lineReader = require('line-reader');

var fs = require('fs');
var src,dst,bc=97,slt,slg,elt,elg;
var $ = jQuery = require('jquery')(window);

app.use(express.static('public'))
app.use(methodOverride("_method"));
app.use(bodyParser.urlencoded({extended:true}));


app.get("/",function(req,res){
	res.render("start.ejs");
});

var ptr = 0,i=0;





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
          // console.log(data["results"][0]["locations"][0]["latLng"]["lat"]);
          src = loc;
          console.log(data["results"][0]["locations"][0]["latLng"]["lat"]);
          slt = data["results"][0]["locations"][0]["latLng"]["lat"]
          slg = data["results"][0]["locations"][0]["latLng"]["lng"]
         for(var i=0;i<data["results"][0]["locations"].length;++i)
          		if(data["results"][0]["locations"][0]["adminArea5"]=="" ||data["results"][0]["locations"][0]["adminArea5"]==undefined)
          		 		if(data["results"][0]["locations"][0]["adminArea3"]=="" ||data["results"][0]["locations"][0]["adminArea3"]==undefined){
          		 			continue;
          		 		}
          		 		else 
          		 		{
          		 			src = data["results"][0]["locations"][0]["adminArea3"];
          		 			break;
          		 		}
          		else
          		{
          			src = data["results"][0]["locations"][0]["adminArea5"];
          			break;
          		}
          console.log(src);

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
          dst = loc;
          console.log(data["results"][0]["locations"][0]["latLng"]["lat"]);
          elt = data["results"][0]["locations"][0]["latLng"]["lat"]
          elg = data["results"][0]["locations"][0]["latLng"]["lng"]
          for(var i=0;i<data["results"][0]["locations"].length;++i)
          		if(data["results"][0]["locations"][0]["adminArea5"]=="" ||data["results"][0]["locations"][0]["adminArea5"]==undefined)
          		 		if(data["results"][0]["locations"][0]["adminArea3"]=="" ||data["results"][0]["locations"][0]["adminArea3"]==undefined){
          		 			continue;
          		 		}
          		 		else 
          		 		{
          		 			dst = data["results"][0]["locations"][0]["adminArea3"];
          		 			break;
          		 		}
          		else
          		{
          			dst = data["results"][0]["locations"][0]["adminArea5"];
          			break;
          		}

          	var spawn = require("child_process").spawn; 
          	// var process = spawn('python',["/home/kush/projects/sih/public/data.py",slt,slg,elt,elg]); 
          	var process = spawn('python',["/home/kush/projects/sih/data.py",slt,slg,elt,elg]);
          	process.stdout.on('data', function(data) { 
	          console.log(data.toString()); 
            res.redirect("/final");
	        });
          	
          	process.stderr.on('data', function(data) { 
          console.log(data.toString());
          console.log("I'm Back ");
          });

            
        }
      });
          // $("#from").html(src);
        }
      })

		// res.render("index.ejs",{from:src,to:dst});
});
app.get("/final",function(req,res){
	res.render("tmp.ejs",{from:src,to:dst,bc:bc});

});

app.get("/wait",function(req,res){
	res.render("wait.ejs");
})
app.get("/return",function(req,res){
	fs.readFile('data', 'utf8', function(err, contents) {
});
	res.json({"sexyBitch":"me"});
})

app.listen(3000,function(){
	console.log("Server started");
});










