/*var form = document.forms.namedItem("fileinfo");
form.addEventListener('submit', function(ev) {

    var oOutput = document.getElementById('#output1');
    var oData = new FormData(form);
    alert("got here");    
    oData.append("CustomField", "This is some extra data");
    alert(oData.getAll('url'));
    var url = oData.getAll('url');
    var form = new FormData();
    form.append("src", "https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg");
    form.append("", "");
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://localhost:5000/process/src/url",
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
});
*/

/*
function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function (e) {
                $('#blah').attr('src', e.target.result);
            }
            
            reader.readAsDataURL(input.files[0]);
        }
    }
    
$("#imgInp").change(function(){
    readURL(this);
});

*/
/*
+ function($) {
    'use strict';

    // UPLOAD CLASS DEFINITION
    // ======================

    var dropZone = document.getElementById('drop-zone');
    var uploadForm = document.getElementById('js-upload-form');

    var startUpload = function(files) {
        console.log(files.name)
    }

    var form = document.forms.namedItem("js-upload-form");
    uploadForm.addEventListener('submit', function(e) {
        var uploadFiles = document.getElementById('js-upload-files');
        oData = new FormData(uploadFiles);
        oData.name;
        e.preventDefault()


        startUpload(uploadFiles)
    })

    dropZone.ondrop = function(e) {
        e.preventDefault();
        this.className = 'upload-drop-zone';

        startUpload(e.dataTransfer.files)
    }

    dropZone.ondragover = function() {
        this.className = 'upload-drop-zone drop';
        return false;
    }

    dropZone.ondragleave = function() {
        this.className = 'upload-drop-zone';
        return false;
    }

}(jQuery);


*/