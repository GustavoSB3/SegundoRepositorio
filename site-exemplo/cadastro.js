const $html = document.querySelector('html')
const $checkbox = document.querySelector('#switch')

const $formCadastrar = document.querySelector('#cadastrar-form')
$formCadastrar.addEventListener('submit', event=>{
    event.preventDefault()


    
    const email = document.querySelector('#email').value
    const senha = document.querySelector('#senha').value
    const repet = document.querySelector('#repet').value

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
  console.log(data);
})
.catch(error => {
  console.error("Erro ao cadastrar:", error);
});

});