// fetch monto ingresos
fetch('http://127.0.0.1:5001/movimientos/montoingresos')
  .then(response => response.json())
  .then(totalingresos => {
      document.getElementById('ingresostotales2').innerHTML = totalingresos[0]["Ingresos totales"]
      console.log(totalingresos)})


// fetch monto gastos

fetch('http://127.0.0.1:5001/movimientos/montogastos')
   .then(response => response.json())
  .then(totalgastos => {
      document.getElementById('gastostotales2').innerHTML = totalgastos[0]["Gastos totales"]
      console.log(totalgastos)})

