
const btn = Array.from(document.querySelectorAll(".btn"));
const ac = document.getElementById("ac");
const ce = document.getElementById("ce")
const equal = document.getElementById("equal");
const display = document.getElementById("display");
function clearDisplay() {
  display.innerText = "0";
}
function calculate() {
  let num = Number(eval(display.innerText).toFixed(5));
  display.innerText = num;
}
function displayFunc(eve) {
  const value = eve.target.value;
    if(display.innerText === "0"){
        display.innerText = value;
    }
    else{
  display.innerText += value;
}}
function clearValue(){
    const Number = display.innerText;
    if(display.innerText.length ===1){
        display.innerText ='0';
    }
    else{
    display.innerText = Number.slice(0,-1);
}}
function start() {
//   clearDisplay();

  btn.forEach((elem) => elem.addEventListener("click", displayFunc));
  ac.removeEventListener("click", displayFunc);
  ac.addEventListener("click", clearDisplay);
  ce.removeEventListener("click", displayFunc);
  ce.addEventListener('click',clearValue)
  equal.removeEventListener("click", displayFunc);
  equal.addEventListener("click", calculate);
}
start();
