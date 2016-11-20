
var formElementName = "form";
var serverAddr = "http://127.0.0.1:5000";

$(':file').change(function(){
    var file = this.files[0];
    var name = file.name;
    var size = file.size;
    var type = file.type;
});

function progressHandlingFunction(e){

}

var processFromFile = function()
{
    var formData = new FormData($(formElementName)[0]);
    $.ajax({
        url: serverAddr+'/process/src/file',  //Server script to process data
        type: 'POST',
        xhr: function() {  // Custom XMLHttpRequest
            var myXhr = $.ajaxSettings.xhr();
            if(myXhr.upload){ // Check if upload property exists
                myXhr.upload.addEventListener('progress',progressHandlingFunction, false); // For handling the progress of the upload
            }
            return myXhr;
        },
        //Ajax events
        success: function(a) { console.log("suc"); },
        error: function(a) { console.log("err"); },
        // Form data
        data: formData,
        //Options to tell jQuery not to process data or worry about content-type.
        cache: false,
        contentType: false,
        processData: false,
        crossDomain: true
    });
}

var processFromUrl = function()
{
    var form = new FormData();
    form.append("src", "https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg");
    form.append("", "");
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": serverAddr+"/process/src/url",
        "method": "POST",
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": form,
        success: function(data) { console.log(data); },
        error: function(data) { alert("err"); }
    }

    $.ajax(settings).done(function (response) {
         alert("recived response");
         console.log(response);
     });
}