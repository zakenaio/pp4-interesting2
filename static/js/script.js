$(document).ready(function () {
    // JavaScript code for handling vote registration and displaying popup
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
                // Assuming the element that displays the vote count has a class 'vote-count'
                // and is a sibling of the clicked '.vote-icon'
                $this.siblings('.vote-count').text(response.votes);
            },
            error: function (xhr, status, error) {
                // Handle any errors
            }
        });
    });
});

// JavaScript for handling comment form submission
$(document).ready(function () {
    $('#comment-form').on('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Serialize the form data
        var formData = $(this).serialize();

        // Make an AJAX request to submit the form data
        $.ajax({
            url: $(this).attr('action'), // Use the form's action attribute as the URL
            method: $(this).attr('method'), // Use the form's method attribute as the HTTP method
            data: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function (response) {
                // Update the page with the new comment
                // Replace 'comment-section' with the ID of the element where comments are displayed
                $('#comment-section').append('<li><strong>' + response.author_name + '</strong>: ' + response.text + '</li>');
                // Clear the form after successful submission
                $('#comment-form')[0].reset();
            },
            error: function (xhr, status, error) {
                // Handle any errors
                console.error('Error:', error);
            }
        });
    });
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

window.addEventListener('scroll', function () {
    var navbar = document.querySelector('.navbar');
    var scrollPosition = window.scrollY;

    // Adjust the scroll position threshold as needed
    if (scrollPosition > 400) {
        // Add a CSS class to the navbar when the scroll position is greater than 100px
        navbar.classList.add('dark-background');
    } else {
        // Remove the CSS class when the scroll position is less than 100px
        navbar.classList.remove('dark-background');
    }
});

// Define arrow before using it
let arrow = document.querySelector('.arrow');


// Show/hide the arrow based on the scroll position
window.addEventListener('scroll', function () {
    var scrollPosition = window.scrollY;
    var maxScroll = window.innerHeight;

    // Calculate the opacity based on the scroll position
    var opacity = 1 - (scrollPosition / maxScroll);

    // Set the calculated opacity for the arrow, if it exists
    if (arrow) {
        arrow.style.opacity = opacity;
    }
});