const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')


$checkbox.addEventListener('change', ()=> {
    $html.classList.toggle('dark-mode');
})

const $form = document.querySelector('#login-form')
$form.addEventListener('submit', event=>{
    event.preventDefault()
    const email = document.querySelector('#email').value
    const senha = document.querySelector('#senha').value

    

    fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email,
            senha: senha
        })
    }).then(response=> response.json())
    .then(data => {
        if(data.status === "sucesso") {
            alert("login realizado com sucesso");
        } else {
            alert("Senha ou usuário incorreto")
        }
    })


    console.log(email, senha)
    
})



