$(function() {

    var input = $('#next > input');
    var btn = $('#next > button');
    var instructionDiv = $('#instruction');
    var expressionDiv = $('#expression');
    var scoreDiv = $('#score');
    var errorDiv = $('#error');

    btn.on('click', function() {
        $.ajax({
            type: "POST",
            url: '/game',
            data: {text: input.val()},
            error: function(jqXHR, textStatus, errorThrown) {
                errorDiv.text("There was a problem communicating your request. "+
                    errorThrown);
                errorDiv.show();
            },
            success: function(data) {
                if(typeof data.instruction === 'string') {
                    instructionDiv.text(data.instruction);
                    instructionDiv.show();
                } else {
                    instructionDiv.hide();
                }
                if(typeof data.expression === 'string') {
                    expressionDiv.text(data.expression);
                    expressionDiv.show();
                    if(typeof data.score !== 'string') {
                        input.show();
                    }
                } else {
                    expressionDiv.hide();
                    input.hide();
                }
                if(typeof data.error === 'string') {
                    errorDiv.text(data.error);
                    errorDiv.show();
                } else {
                    errorDiv.hide();
                }
                if(typeof data.score === 'string') {
                    scoreString = "<p>"
                    components = data.score.split('\n');
                    for(i = 0; i < components.length; ++i) {
                        scoreString += components[i] + "</p>"
                    }
                    scoreDiv.html(scoreString);
                    scoreDiv.show();
                    input.hide();
                } else {
                    scoreDiv.hide();
                }
            },
            dataType: "json"
        });
    });
});
