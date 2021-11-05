
 let url2 = 'http://127.0.0.1:5001/movimientos/Ingreso'
        fetch(url2)
            .then(response => response.json())
            .then(data => mostrar2Data(data))
            .catch(error => console.log(error))

        const mostrar2Data = (data) => {
            console.log(data)
            let body = ''
            for (let i = 0; i<data.length; i++){
                body += `<tr><td>${data[i].Fecha}</td><td>${data[i].Categoria}</td><td>${data[i].Concepto}</td><td>${data[i].Monto}</td></tr>`
            }
            document.getElementById('tablaingresos').innerHTML = body
        }
