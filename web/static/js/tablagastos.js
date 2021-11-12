 let urltablagastos = 'http://127.0.0.1:5001/movimientos/Gasto'
        fetch(urltablagastos)
            .then(response => response.json())
            .then(data => mostrarData3(data))
            .catch(error => console.log(error))

        const mostrarData3 = (data) => {
            console.log(data)
            let body = ''
            for (let i = 0; i<data.length; i++){
                body += `<tr><td>${data[i].Fecha}</td><td>${data[i].Categoria}</td><td>${data[i].Concepto}</td><td>${data[i].Monto}</td></tr>`
            }
            document.getElementById('tablagastos').innerHTML = body
        }

