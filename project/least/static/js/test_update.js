$(document).on('click', '.step', function() {
    $('input[name=destination]').val($(this).data('reverse'));
    $('#update-test').submit();
});

$(document).on('click', '.test-next-btn', function() {
    $('#update-test').submit();
});