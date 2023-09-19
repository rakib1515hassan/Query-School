var studentUrl = myData.studentUrl;
$(document).ready(function() {
    $("#add-student-form").submit(function(e) {
        e.preventDefault();

        if (!$("#s_birth").val()) {
            document.getElementById('alart_msg').innerHTML = '<div class="alert alert-danger" role="alert">Birthdate is required. </div>';
        }
        else{
            var formData = {
                s_name:   $("#s_name").val(),
                s_gender: $("#s_gender").val(),
                s_class:  $("#s_class").val(),
                s_roll:   $("#s_roll").val(),
                s_age:    $("#s_age").val(),
                s_city:   $("#s_city").val(),
                s_birth:  $("#s_birth").val(),
    
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val() // Add the CSRF token
    
            };
            
    
            // console.log("Data = ", $("#s_birth").val())
            if(formData) {
                $.ajax({
                    type: 'POST',
                    url: studentUrl,
                    data: formData,
                    success: function(response) {
                        // console.log("Response =", response.message);
        
                        if (response.success) {
                            // Clear form fields
                            $("#s_name").val('')
                            $("#s_gender").val('')
                            $("#s_class").val('')
                            $("#s_roll").val('')
                            $("#s_age").val('')
                            $("#s_city").val('')
                            $("#s_birth").val('')
        
                            // Display success message
                            document.getElementById('alart_msg').innerHTML = '<div class="alert alert-success" role="alert">' + response.message + '</div>';
                        } else {
                            // Handle the case where there was an error
                            // console.error(response.message);
                            document.getElementById('alart_msg').innerHTML = '<div class="alert alert-danger" role="alert">' + response.message + '</div>';
                        }
                    },
                    error: function(xhr) {
                        if (xhr.responseJSON && xhr.responseJSON.message) {
                            document.getElementById('alart_msg').innerHTML = '<div class="alert alert-danger" role="alert">' + xhr.responseJSON.message + '</div>';
                        } else {
                            document.getElementById('alart_msg').innerHTML = '<div class="alert alert-danger" role="alert">An error occurred.</div>';
                        }
                    }
                });
            }
        }


        
    });
});
