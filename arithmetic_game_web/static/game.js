$(function() {

    var input = $('#next > input');
    var btn = $('#next > button');
    var errorDiv = $('#error');

    btn.on('click', function() {
        $.ajax({
            type: "POST",
            url: '/game',
            data: {text: input.val()},
            error: function(jqXHR, textStatus, errorThrown) {
                errorDiv.text("There was a problem communicating your request. "+
                    errorThrown);
            },
            success: function(data) {
                console.log(data);
            },
            dataType: "json"
        });
    });
});
