var teacherUrl = myData.teacherUrl;

$(document).ready(function() {
    $("#add-teacher-form").submit(function(e) {
        e.preventDefault();

        if (!$("#t_join").val()) {
            document.getElementById('alart_msg').innerHTML = '<div class="alert alert-danger" role="alert">Joining Date is required. </div>';
        }
        else {
            var formData = {
                t_name:       $("#t_name").val(),
                t_emplyee_id: $("#t_emplyee_id").val(),
                t_city:       $("#t_city").val(),
                t_salary:     $("#t_salary").val(),
                t_join:       $("#t_join").val(),
                
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val() // Add the CSRF token
            };
    
            if (formData){
                $.ajax({
                    type: 'POST',
                    url: teacherUrl,
                    data: formData,
                    success: function(response) {
                        if (response.success) {
                            // console.log("Response =", response.message);
        
                            // Clear form fields
                            $("#t_name").val('');
                            $("#t_emplyee_id").val('');
                            $("#t_city").val('');
                            $("#t_salary").val('');
                            $("#t_join").val('');
        
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
