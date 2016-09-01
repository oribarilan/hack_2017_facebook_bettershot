var form = document.forms.namedItem("fileinfo");
form.addEventListener('submit', function(ev) {

  var oOutput = document.getElementById('#output1'),
      oData = new FormData(form);

  oData.append("CustomField", "This is some extra data");
  alert(oData.getAll('url'));
  var url = oData.getAll('url');
  alert("sending");
  $.ajax({
        url: "https://7994f3d8.ngrok.io/process/src/url",
        type: 'POST',
        async: true,
        data: {"src" : "https://upload.wikimedia.org/wikipedia/commons/6/67/Inside_the_Batad_rice_terraces.jpg"},
        dataType: 'json', // added data type
    }).done(function( html ) {
   console.log("yo");
  });


}, false);

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