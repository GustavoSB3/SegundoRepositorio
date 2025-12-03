const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

const $formCadastrar = document.querySelector('#cadastrar-form')
$formCadastrar.addEventListener('submit', event=>{
    event.preventDefault()


    
    const email = document.querySelector('#email').value
    const senha = document.querySelector('#senha').value
    const repet = document.querySelector('#repet').value
    const regex = /^(?=(?:.*?[A-Z]){3})(?=(?:.*?[0-9]){2})(?=(?:.*?[!@#$%*()_+^&}{:;?.]){1})(?!.*\s)[0-9a-zA-Z!@#$%;*(){}_+^&]*$/;

fetch("http://127.0.0.1:5000/cadastrarnovo", {
  method: "POST",
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email, senha, repet
  })
})
.then(response => response.json())
.then(data => {
  if(data.status === "sucesso") {
    alert("Usuário criado com sucesso!")
  }

  if (senha.length < 8)
  {

    document.querySelector('#senha').focus();
    return;
  }
  
  {
    if(!regex.exec(senha)){
      const ErrorPassword = document.getElementById('ErrorPassword');


   e.preventDefault()
   ErrorPassword.sytle.display = "block";
   ErrorPassword.textContent =    
   "A senha deve conter no mínimo 1 caracter maiúsculo, 2 números e 1 caracter especial!"
    document.querySelector('#senha').focus();

  return false;
  
    }
}

  return true;

  console.log(data)
  
})
.catch(error => {
  console.error("Erro ao cadastrar:", error)
  
});

 
});