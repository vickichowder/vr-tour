// Register Form
//----------------------------------------------
// Validation
$("#register-form").validate({
  rules: {
    username: "required",
    password: {
      required: true,
      minlength: 5
    },
    password_confirm: {
      required: true,
      equalTo: "#register-form [name=reg_password]"
    },
    email: {
      required: true,
      email: true
    },
    agree: "required",
  },
  errorClass: "form-invalid",
  errorPlacement: function( label, element ) {
    if( element.attr( "type" ) === "checkbox" || element.attr( "type" ) === "radio" ) {
      element.parent().append( label ); // this would append the label after all your checkboxes/labels (so the error-label will be the last element in <div class="controls"> )
    }
    else {
      label.insertAfter( element ); // standard behaviour
    }
  }
});

// Form Submission
$("#register-form").submit(function() {
  remove_loading($(this));

  if(options['useAJAX'] == true)
  {
    // Dummy AJAX request (Replace this with your AJAX code)
    // If you don't want to use AJAX, remove this
    dummy_submit_form($(this));

    // Cancel the normal submission.
    // If you don't want to use AJAX, remove this
    return false;
  }
});
