function message_error(obj){
    var html = ''
    if(typeof (obj) == 'object'){
        html = '<ul style="text-aling: left;">';
        $.each(obj, function(key, value){
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>'
    }else{
        html = '</p>' + obj + '</p>';
    }
    
    Swal.fire({
        title: 'Error!',
        html: html,
        icon: "error",
        // footer: '<a href="#">Why do I have this issue?</a>'
    });
}