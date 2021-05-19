
$(document).ready(function() {
    console.log('Bro')

    $('#generate-button').click(function(e){
        e.preventDefault();
        var type = $("#type").val();
        var count = $("#count").val();

        $('#results').html("");
        $('#full-text').html("");

        axios.get(`/api/${type}/${count}`).then(function (response) {
            var raw = response.data.raw;

            raw.forEach(item => {
                $('#results').append(`<li>${item}</li>`);
            });

            $('#full-text').html(response.data.full);
        });
        
    });
})
