var fs = require('fs');
var path = require('path');
var render = require('../../src/render');

function generateWishListPage ( nameKey ) {
    //will read the data-2018.json file, use the name key to find the phone number and wish list and generate the HTML file
    //will move the files to the public folder which will be reachable via a specific url
    
    var filePath = path.resolve(__dirname + "../../shared/data-2018.json");
    var fileContent = fs.readFileSync(filePath, 'utf-8');
    var allPeople = JSON.parse(fileContent);

    //will generate all the pages
    Object.keys(allPeople).forEach( function (people){
        //for each people name we will make new page in the public folder
        //will need to make the li items and possibly the anchors here as well
        console.log(allPeople[people])


        var values = {
            'fullName': allPeople[people].fullName,
            'wishList': makeList(allPeople[people].wishList)
        };

        var fileOutput = render.constructPage("/template/index.html", {}, values);
        //must make a random page number
        console.log(__dirname)
        fs.writeFile(__dirname +"../../public/"+people+ Math.floor((Math.random() * 100)) +'.html', fileOutput, function(err) {
            if(err) {
                return console.log(err);
            }
        
            console.log("The file was saved!");
        }); 
    })
}

function makeList (listItems) {
    var listStr = "";
    listItems.forEach( value => {
        if(typeof value === 'string'){
            //means we append to listItems of
            listStr +="<li>"+value+"</li>"
        }
        else if ( value.href && value.name) {
            listStr+= "<li><a href='"+ value.href+"'>"+ value.name+ "</a></li>"
        }
    })
    return listStr;
}

generateWishListPage();