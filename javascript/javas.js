var botao = document.getElementById("botao");
botao.addEventListener("click", function () {
  var nome = document.getElementById("nome");

  var sabor = document.getElementById("sabor");

  if (nome.value.trim() === "") {
    alert("coloque seu nome");
  } else if (sabor.selectedIndex === 0) {
    alert("coloqueselecione o sabor");
  } else {
    var htmlescr =
      "Senhor " +
      nome.value +
      "\nseu sorvete de " +
      sabor.value +
      " esta sendo preparado"; //ignora a desoranisação que esse é um dos primeiros java scripts

    var resultado = document.getElementById("result");

    var textapr = document.createElement("invtxt");
    textapr.textContent = htmlescr;

    resultado.appendChild(textapr);
  }
});
