$(document).ready(function () {
    // Vote system
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
$(document).ready(function () {
    $('#comment-form').on('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission
        
        var formData = $(this).serialize();

        // Make an AJAX request to submit the form data
        $.ajax({
            url: $(this).attr('action'), 
            method: $(this).attr('method'), 
            data: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            success: function (response) {
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

// Create News
document.getElementById('createNewsForm').addEventListener('submit', function(e) {
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
        // Handle response data (e.g., close modal, show message)
        console.log(data);
    })
    .catch(error => {
        // Handle errors
        console.error('Error:', error);
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

    if (scrollPosition > 200) {
        navbar.classList.add('dark-background');
    } else {
        navbar.classList.remove('dark-background');
    }
});

let arrow = document.querySelector('.arrow');


window.addEventListener('scroll', function () {
    var scrollPosition = window.scrollY;
    var maxScroll = window.innerHeight;

    var opacity = 1 - (scrollPosition / maxScroll);

    if (arrow) {
        arrow.style.opacity = opacity;
    }
});