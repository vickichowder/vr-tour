$(function(){
    $('#btnWeAte').click(function(){
        
        $.ajax({
            url: '/weAte',
            data: {},
            type: 'POST',
            success: function(response){
                console.log(response);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});