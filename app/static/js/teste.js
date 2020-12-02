function UploadFile(form) {
    var formData = new FormData(form);    
    $.ajax({
         url: 'getfile',
         type: 'POST',
         data: formData,
         async: true,
         cache: false,
         contentType: false,
         enctype: 'multipart/form-data',
         processData: false,
         success: function (data) {
             var listaSetores = $('#cars');
            for (var prop in data.lyrs) {
              listaSetores.append('<option value="'+ prop +'">'+ prop +'</option>');              
              console.log(prop);
            }        
         }         
    });
}

$("#send").click(function (e) {    
    e.preventDefault();    
    var forms = $("#fileUpload");
    alert(forms.length);
    for (var i = 0; i < forms.length; i++) {
        UploadFile(forms[i]);

    }
});


//$("document").ready(function(){
//    $("#send").click(function(){
//        var message = $("#message").val();
//        console.log("sdsdsds");
//        $.ajax({
//            url: "getfile",
//            type: "POST",
//            contentType: "application/json",
//            data: JSON.stringify({"message": message})
//        }).done(function(data) {
//            console.log(data);
//            document.getElementById('texto').innerHTML = data['message'];
//        });
//    });
//});

//$(function () {
//
//    var form;
//    $('#fileUpload').change(function (event) {
//        form = new FormData();
//        form.append('fileUpload', event.target.files[0]); // para apenas 1 arquivo
//        //var name = event.target.files[0].content.name; // para capturar o nome do arquivo com sua extenção
//    });
//
//    $('#btnEnviar').click(function () {
//        $.ajax({
//            url: 'getfile', // Url do lado server que vai receber o arquivo
//            data: form,
//            processData: false,
//            contentType: false,
//            type: 'POST',
//            success: function (data) {
//                console.log(data)
//            
//            var listaSetores = $('#cars');
//            for (var prop in data.lyrs) {
//              listaSetores.append('<option value="'+ prop +'">'+ prop +'</option>');              
//              console.log(prop);
//            }                
//            }
//        });
//    });
//});
//

