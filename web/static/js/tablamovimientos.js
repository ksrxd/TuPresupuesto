 let url = 'http://127.0.0.1:5001/movimientos'
        fetch(url)
            .then(response => response.json())
            .then(data => mostrarData(data))
            .catch(error => console.log(error))

        const mostrarData = (data) => {
            console.log(data)
            let body = ''
            for (let i = 0; i<data.length; i++){
                body += `<tr><td>${data[i].Fecha}</td><td>${data[i].TipoMovimiento}</td><td>${data[i].Categoria}</td><td>${data[i].Concepto}</td><td>${data[i].Monto}</td></tr>`
            }
            document.getElementById('tablamovimientos').innerHTML = body
        }

