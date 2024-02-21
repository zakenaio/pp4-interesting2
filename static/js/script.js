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

// Comments
$('.comment-form').on('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    var formData = $(this).serialize();

    $.ajax({
        url: $(this).attr('action'), 
        method: $(this).attr('method'), 
        data: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
        success: function (response) {
            // Append the new comment to the list of comments
            $('.comments-list').append('<li>' + response.author_name + ': ' + response.text + '</li>');
            // Clear the form fields
            $('.comment-form')[0].reset();
            // Display the success message with SweetAlert2
            Swal.fire({
                title: 'Success!',
                text: 'Your comment has been added successfully, to view it you need to reload the page for now.',
                icon: 'success',
                confirmButtonText: 'Cool'
            });
        },
        error: function (xhr, status, error) {
            // Handle any errors
            console.error('Error:', error);
            // Optionally, display an error message with SweetAlert2
            Swal.fire({
                title: 'Error!',
                text: 'There was an error posting your comment.',
                icon: 'error',
                confirmButtonText: 'OK'
            });
        }
    });
});


// Create News
document.addEventListener('DOMContentLoaded', function() {
    var createNewsForm = document.getElementById('createNewsForm');
    if (createNewsForm) {
        createNewsForm.addEventListener('submit', function(e) {
            e.preventDefault();
            var formData = new FormData(this);
            
            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});

// Function to retrieve CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name matches the expected format
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Include CSRF token in AJAX request headers
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
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
