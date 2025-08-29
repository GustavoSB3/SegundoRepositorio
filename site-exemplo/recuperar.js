const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

const $recuperar = document.querySelector('#recuperar')
$recuperar.addEventListener('submit', event=>{
    event.preventDefault()
    const email = document.querySelector('#email').value
    
    fetch("http://127.0.0.1:5000/recuperarsenha", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
        })
    }).then(response=> response.json())


    console.log(email)
    
})