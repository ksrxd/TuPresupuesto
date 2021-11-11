fetch('http://127.0.0.1:5001/movimientos/montoingresos')
  .then(response => response.json())
  .then(data => console.log(data));
  .catch(function() {

});
