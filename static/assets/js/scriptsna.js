$(document).on('submit', '#formAut', function(e){
    toastr.options = {
        "closeButton": true,
        "debug": false,
        "positionClass": "toast-bottom-full-width",
        "onclick": null,
        "showDuration": "3000",
        "hideDuration": "1000",
        "timeOut": "5000",
        "extendedTimeOut": "1000",
        "showEasing": "swing",
        "hideEasing": "linear",
        "showMethod": "fadeIn",
        "hideMethod": "fadeOut"
    }
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/investigador/registrarAut/',
        data:{
            email: $('#email').val(),
            name: $('#name').val(),
            lastname: $('#lastname').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            $('#autorNew').modal('hide');
            $('#email').val('');
            $('#name').val('');
            $('#lastname').val('');
            toastr.info("Se ha registrado correctamente en la base de datos.","Autor registrado");
            $.each(data, function(index, item) {
                var newOption = "<option value='" + item.value + "'>" + item.text + "</option>";
                $(".autores").append(newOption);
            });
        },
        error : function(){
            $('#email').val('');
            $('#name').val('');
            $('#lastname').val('');
            toastr.error("El correo electronico ya se encuentra registrado en la base de datos.","ERROR");
        }
    });
});
