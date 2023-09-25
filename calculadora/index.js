document.addEventListener("DOMContentLoaded", function () {
  var botao = document.querySelector(".bot");
  var n1 = document.getElementById("n1");
  var op = document.getElementById("op");
  var n2 = document.getElementById("n2");
  var result;
  var cresult = document.getElementById("result");
  op.addEventListener("change", function () {
    if (op.selectedIndex === 6) {
      n2.style.visibility = "hidden";
      cresult.style.left = "-80px";
      botao.style.left = "-80px";
    } else {
      n2.style.visibility = "visible";
      cresult.style.left = "0px";
      botao.style.left = "0px";
    }
  });

  botao.addEventListener("click", function () {
    var fn1 = parseFloat(n1.value);
    var fn2 = parseFloat(n2.value);
    if (op.selectedIndex === 0) {
      alert("escolha uma operação");
    }
    if (op.selectedIndex === 1) {
      result = fn1 + fn2;
    } else if (op.selectedIndex === 2) {
      result = fn1 - fn2;
    } else if (op.selectedIndex === 3) {
      result = fn1 * fn2;
    } else if (op.selectedIndex === 4) {
      result = fn1 / fn2;
    } else if (op.selectedIndex === 5) {
      result = fn1 ** fn2;
    } else if (op.selectedIndex === 6) {
      result = fn1 ** (1 / 2);
    }
    cresult.value = result;
  });
});
