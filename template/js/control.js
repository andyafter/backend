function submit(){
    var f = document.getElementById("#inputform");
    console.log($("inputform").serialize());
    console.log("success");
}


$(document).ready(function () {

});

$("#inputform").keydown(function(event) {
    console.log("success");
    if (event.which == 13) {
        event.preventDefault();
	console.log("success");
        //$("form").submit();
    }
});


function test(){
    var a = document.getElementById('taginput').value;
    console.log(a);
    var url = "http://172.23.186.250:5000/search/";
    var h = "%23";
    var table = document.getElementById("mytable");
    var row ;//= table.insertRow(0);
    var cells=[];
    var xmlHttp = new XMLHttpRequest();

    /*
    cells[0] = row.insertCell(0);
    cells[1] = row.insertCell(1);
    cells[2] = row.insertCell(2);
    cells[3] = row.insertCell(3);
    cells[4] = row.insertCell(4);
    cells[0].innerHTML = "Tag Name";
    cells[1].innerHTML = "Count" ;
    cells[2].innerHTML = "Positive";
    cells[3].innerHTML = "Negative";
    cells[4].innerHTML = "Neutral";
    */
    while(table.rows.length > 0) {
	table.deleteRow(0);
    }
    row =  table.insertRow(0);;
    //return xmlHttp.responseText;
    //console.log(a[0]);
    if(a[0]=='#'){
	//console.log(a.substring(1,a.length)); // that's the right form
	url+=h;
	url+=a.substring(1,a.length);
    }
    else{
	url+=a;
    }
    xmlHttp.open( "GET", url, false );
    xmlHttp.send( null );
    //console.log(xmlHttp.responseText[1]);
    var text = xmlHttp.responseText;
    var result = JSON.parse(text);
    //console.log(result[0][result[1][1]]);
    for(var i=0;i<result[1].length;i++){
	row = table.insertRow(i+1);
	for(var j=0;j<5;j++){
	    cells[j] = row.insertCell(j);
	    //cells[j].innerHTML = result[0][result[1]];
	}
	cells[0].innerHTML = result[1][i];
	cells[1].innerHTML = result[0][result[1][i]].count;
	cells[2].innerHTML = result[0][result[1][i]].positive;
	cells[3].innerHTML = result[0][result[1][i]].negative;
	cells[4].innerHTML = result[0][result[1][i]].neutral;
    }
    //cell1.innerHTML = "hashtag";
}
