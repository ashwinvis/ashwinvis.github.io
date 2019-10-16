$(document).foundation();

if ($(window).width() > 960) {
    $('#foot').css('margin-top', 0);        
    var h = $(document).height() - $('#content1').height() - $('#foot').height()
    if ( h < 0 ) { h = 0 };
    $('#foot').css('margin-top', h);
}

$(window).bind("resize", function() {
    if ($(window).width() > 960) {
        $('#foot').css('margin-top', 0);        
        var h = $(document).height() - $('#content1').height() - $('#foot').height()
        if ( h < 0 ) { h = 0 };
        $('#foot').css('margin-top', h);
    }
});


