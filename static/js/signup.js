$(function() {
    $('#btnSignUp').click(function() {
	console.log("signUp clicked!!!")
	alert("called!!!")
	$.ajax({
	    url: '/signUp',
	    data: $('form').serialize(),
	    type: 'POST',
	    success: function(response) {
		console.log(response);
	    },
	    error: function(error) {
		console.log(error);
	    }
	});
    });
});

$(function() {
    $('#btnSignIn').click(function() {
	console.log("signIn Called!!!")
	alert("called!!!")
	$.ajax({
	    url: '/signIn',
	    data: $('form').serialize(),
	    type: 'POST',
	    success: function(response) {
		console.log(response);
	    },
	    error: function(error) {
		console.log(error);
	    }
	});
    });

});
