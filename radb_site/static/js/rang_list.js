$(document).ready(function() {
    $('#prni').show();

    $('#btn_rtrk').click(function(){
        $('#btn_prni').removeClass('active');
        $('#btn_auto').removeClass('active');
        $('#prni').hide();
        $('#auto').hide();

        $(this).addClass('active');
        $('#rtrk').show();
    });

    $('#btn_prni').click(function(){
        $('#btn_rtrk').removeClass('active');
        $('#btn_auto').removeClass('active');
        $('#rtrk').hide();
        $('#auto').hide();

        $(this).addClass('active');
        $('#prni').show();
    });

    $('#btn_auto').click(function(){
        $('#btn_rtrk').removeClass('active');
        $('#btn_prni').removeClass('active');
        $('#rtrk').hide();
        $('#prni').hide();

        $(this).addClass('active');
        $('#auto').show();
    });
})


