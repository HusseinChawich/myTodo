async function addListItem() {
    const name = document.getElementById('name').value;
    const response = await fetch('/listitems/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // CSRF protection
        },
        body: JSON.stringify({ name: name })
    });

    if (response.ok) {
        const data = await response.json();
        alert('Item added: ' + data.name);
    } else {
        alert('Error adding item');
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}