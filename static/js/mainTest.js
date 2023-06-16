$(function(){
    $("#form-register").validate({
        messages: {
            sex: {
                required: "Proszę wybrać płeć"
            },
            BMI: {
                required: "Proszę uzupełnić swoje BMI"
            },
            age: {
                required: "Proszę wybrać datę urodzenia"
            },
            hp: {
                required: "Proszę wybrać ciśnienie krwi"
            },
            smoke: {
                required: "Proszę uzupełnić informacje dotyczące palenia"
            },
            physActivity: {
                required: "Proszę uzupełnić informacje dotyczące aktywności fizycznej"
            },
            fruit: {
                required: "Proszę uzupełnić informacje dotyczące konsumpcji owoców"
            },
            veggie: {
                required: "Proszę uzupełnić informacje dotyczące konsumpcji warzyw"
            },
            generalHealth: {
                required: "Proszę uzupełnić informacje dotyczące ogólnego samopoczucia"
            },
            mentalHealth: {
                required: "Proszę uzupełnić informacje dotyczące samopoczucia psychicznego"
            },
            physHealth: {
                required: "Proszę uzupełnić informacje dotyczące samopoczucia fizycznego"
            }
        }
    });
    $("#form-total").steps({
        headerTag: "h2",
        bodyTag: "section",
        transitionEffect: "fade",
        // enableAllSteps: true,
        autoFocus: true,
        transitionEffectSpeed: 500,
        titleTemplate : '<div class="title">#title#</div>',
        labels: {
            previous : 'Back',
            next : '<i class="zmdi zmdi-arrow-right"></i>',
            finish : '<i class="zmdi zmdi-arrow-right"></i>',
            current : ''
        },
        onStepChanging: function (event, currentIndex, newIndex) { 
            var sex = $('#sex').val();
            var BMI = $('#BMI').val();
            var age = $('#age').val();
            var hp = $('#hp').val();
            var smoke = $('#smoke').val();
            var physActivity = $('#physActivity').val();
            var fruit = $('#fruit').val();
            var veggie = $('#veggie').val();
            var generalHealth = $('#generalHealth').val();
            var mentalHealth = $('#mentalHealth').val();
            var physHealth = $('#physHealth').val();

            $('#sex-val').text(sex);
            $('#BMI-val').text(BMI);
            $('#age-val').text(age);
            $('#hp-val').text(hp);
            $('#smoke-val').text(smoke);
            $('#physActivity-val').text(physActivity);
            $('#fruit-val').text(fruit);
            $('#veggie-val').text(veggie);
            $('#generalHealth-val').text(generalHealth/5);
            $('#mentalHealth-val').text(mentalHealth/5);
            $('#physHealth-val').text(physHealth/5);

            $("#form-register").validate().settings.ignore = ":disabled,:hidden";
            return $("#form-register").valid();
        }
    });
});

// Rating Initialization
$(document).ready(function() {
    $('#rateMe1').mdbRate();
  });