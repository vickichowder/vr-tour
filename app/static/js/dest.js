$(function() {
    $("button").on("click", function() {
        $.ajax({url: "city/" + $(this).text()});
    }
});
