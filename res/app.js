$(function(){
    // hide all tabs, but the first
    $('section').hide();
    $('section:first').show();

    // make tabs clickable
    $('nav button').click(function(){
        $('section').hide();
        $('#'+$(this).data('name')).show();
    });

    $('section button').click(function(){
        var $me = $(this);
        var section = $me.parent().attr('id');
        var button  = $me.data('name');

        console.log('run '+section+' '+button);
    });

});

