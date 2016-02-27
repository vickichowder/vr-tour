$(function() {
    $('#btnweAte').click(function() {
 
        $.ajax({
            url: '/weAte',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});