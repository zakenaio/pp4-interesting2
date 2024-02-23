// Vote system
$(document).ready(function () {
    $('.vote-icon').on('click', function () {
        var postSlug = $(this).data('post-slug');
        var $this = $(this); // Store the clicked element for use in the callback
    
        $.ajax({
            url: '/vote/',
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'slug': postSlug,
            },
            success: function (response) {
                $this.siblings('.vote-count').text(response.votes);
            },
            error: function (xhr, status, error) {
                // Handle any errors
                console.error('Error:', error);
            }
        });
    });
});

// Navbar fade
window.addEventListener('scroll', function () {
    var navbar = document.querySelector('.navbar');
    var scrollPosition = window.scrollY;

    if (scrollPosition > 200) {
        navbar.classList.add('dark-background');
    } else {
        navbar.classList.remove('dark-background');
    }
});

// Arrow
let arrow = document.querySelector('.arrow');

window.addEventListener('scroll', function () {
    var scrollPosition = window.scrollY;
    var maxScroll = window.innerHeight;

    var opacity = 1 - (scrollPosition / maxScroll);

    if (arrow) {
        arrow.style.opacity = opacity;
    }
});

// Sign in Errors in modal
$(document).ready(function() {
    $('#loginForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/accounts/login/',
            type: 'post',
            data: $(this).serialize(),
            success: function(data) {
                window.location.href = '/';
            },
            error: function(xhr, status, error) {
                $('#loginError').text('The username and/or password you specified are not correct.').show();
            }
        });
    });
});

// Sign up Errors in modal
$(document).ready(function() {
    $('#signupForm').on('submit', function(e) {
        e.preventDefault();

        var form = $(this);
        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: form.serialize(),
            success: function(data) {
                window.location.href = '/';
            },
            error: function(xhr) {
                var errorContainer = $('#signUpModal .errorlist');
                errorContainer.empty().hide();

                var response = JSON.parse(xhr.responseText);
                var formErrors = response.form.fields;

                $.each(formErrors, function(fieldName, fieldData) {
                    if (fieldData.errors && fieldData.errors.length > 0) {
                        $.each(fieldData.errors, function(index, errorMessage) {
                            errorContainer.append('<p>' + errorMessage + '</p>').show();
                        });
                    }
                });
            }
        });
    });
});