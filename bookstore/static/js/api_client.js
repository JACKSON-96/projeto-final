fetch('http://127.0.0.1:8000/protected_route/', {
    method: 'GET',
    headers: {
        'Authorization': 'Token 99f7e666b1bd3650befe7dfd9d71e68216f8598b'
    }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
