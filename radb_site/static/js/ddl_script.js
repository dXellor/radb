//DISCLAIMER!
//Puno trash koda sledi
//Ovako se ne prave spregnute dropdown liste, ovo je samo cheat jer znam da ce mi vrednosti koja lista moze imati uvek biti ove cetiri
//Kako se zapravo radi: https://youtu.be/LmYDXgYK1so

function init_ddl2(){
    var values = ["Primenjene računarske nauke i informatika","Računarski upravljački sistemi","Računarska tehnika i računarske komunikacije", "Neopredeljen"];
    var selected_value = $('#MW1').val()
    var mw2_val = $('#MW2').val()

    if(selected_value != 'Neopredeljen'){
        if((selected_value == mw2_val)){
            $('#MW2').find('option').remove().end().append('<option value="Neopredeljen">Neopredeljen</option>').val('Neopredeljen');
        }else{
            var index = values.indexOf(mw2_val);
            if (index !== -1) {
                values.splice(index, 1);
            }
        }
    
        var index = values.indexOf(selected_value);
        if (index !== -1) {
            values.splice(index, 1);
        }
    
        $('#MW2').find('option').each(function() {
            if ( $(this).val() == selected_value ) {
                $(this).remove();
            }
        });
        
        $(values).each(function() {
            $('#MW2').append($("<option>")
            .prop('value', this)
            .text(this));
        });
        
    }else{
        $('#MW2').find('option').remove().end().append('<option value="Neopredeljen">Neopredeljen</option>').val('Neopredeljen');
    }
}

$(document).ready(function() {
    var values = ["Primenjene računarske nauke i informatika","Računarski upravljački sistemi","Računarska tehnika i računarske komunikacije", "Neopredeljen"];
    tr_vrednost = $('#MW1').val()

    var index = values.indexOf(tr_vrednost);
    if (index !== -1) {
        values.splice(index, 1);
    }

    $(values).each(function() {
        $('#MW1').append($("<option>")
        .prop('value', this)
        .text(this));
    });

    init_ddl2()
});

$(document).on('change', '#MW1', init_ddl2);