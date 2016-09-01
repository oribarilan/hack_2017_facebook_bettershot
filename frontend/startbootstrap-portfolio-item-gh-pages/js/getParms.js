var xmlhttp = new XMLHttpRequest();
var url = "http://7994f3d8.ngrok.io/hello";

var displayResult = function(result){
    console.log(result.hello);
    $("#test1").replaceWith("<li>" + result.hello)
}

alert("here!")
$.ajax({
        url: "https://7994f3d8.ngrok.io/hello",
        type: 'GET',
        async: true,
        dataType: 'json', // added data type
        success: function(res) {
            displayResult(res);
            console.log(res);
        }
});
/*
var test = function(){
    alert('called');
    $.ajax({url: url, 
    dataType: "jsonp",
    crossDomain:true,
    success: function(result){
        displayResult(result);
    },
    error: function (xhr, ajaxOptions, thrownError) {
        alert("Aa");
        alert(thrownError);
    }
    });
}

test();


xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        myFunction(myArr);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();

function myFunction(arr) {
    var out = "";
    var i;
    for(i = 0; i < arr.length; i++) {
        console.log(arr[i]);
    }
    document.getElementById("id01").innerHTML = out;
}

*/